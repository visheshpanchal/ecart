from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from accounts.add_view import default_cart

from .models import AuthModel

"""
This use model is depend on Custom User model and Custom Authentication in This App


"""
# Create your views here.
class AccountRegister(View):
    
    """
        Add Cart Structure Default
        CartView = user_id 
                    cart_items -> { products:[ [product_id, category_id] ]  }
    """
    
    
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
            user = AuthModel.objects.create_user(first_name,last_name,email,password1)
            user.save()
            ## Adding Default Cart Structure
            cart = default_cart.default_cart(request,user.id)
            return redirect("home:home_func")
        else :
            return HttpResponse("Wrong Password")
        
        

class AccountLogin(View):
    
    def get(self,request):
        if request.user.is_authenticated :
            return redirect('home:home_func')
        return render(request,"./accounts/login.html")
    
    def post(self,request):
        
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request=request,email=email,password=password)
        
        if user is not None and user.is_authenticated:
            login(request,user)
            
            return redirect("home:home_func")
        
        return HttpResponse("Bad Request")

class Logout(View):
    
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
        
        return redirect('home:home_func')
        

class AccountRemove(View):
    ## delete user account
    ## delete Wishlist structure
    ## delete cart Structure
    
    pass
