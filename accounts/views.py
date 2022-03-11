from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import AuthModel

"""
This use model is depend on Custom User model and Custom Authentication in This App


"""
# Create your views here.
class AccountRegister(View):
    
    def get(self,request:HttpRequest):
        return render(request,"./accounts/register.html")
    
    def post(self,request:HttpRequest):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        city = request.POST['city']
        
        user = None
        if password1 == password2 :
            user = AuthModel.objects.create_user(first_name,last_name,email,city,password1)
            user.save()
            return HttpResponse("Successfully Account Created")
        else :
            return HttpResponse("Wrong Password")
        
        

class AccountLogin(View):
    
    def get(self,request):
        return render(request,"./accounts/login.html")
    
    def post(self,request):
        print("Work -----------------------------------------")
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request=request,email=email,password=password)
        
        if user is not None and user.is_authenticated:
            login(request,user)
            return redirect("home:home_func")
        return HttpResponse("Bad Request")

class Logout(View):
    
    
    def get(self,request):
        
        logout(request)
        
        return redirect('home:home_func')
        
