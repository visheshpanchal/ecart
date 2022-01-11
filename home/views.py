from typing import AnyStr

from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request:HttpRequest):
    if request.method == "GET":
        pass
    
    return render(request,"./home.html")

class Home(object):
    home_page:AnyStr
    
    def get(self,request):
        return HttpResponse("")
