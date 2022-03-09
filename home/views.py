from typing import AnyStr

from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateResponseMixin, View
from product.models import Category

# Create your views here.

# def home(request:HttpRequest):
#     if request.method == "GET":
#         pass
    
#     return render(request,"./home.html")

# class Home(object):
#     home_page:AnyStr
    
#     def get(self,request):
#         return HttpResponse("")

class Home(View,TemplateResponseMixin):
    template_name = "./home.html"
    
    def get(self,request:HttpRequest):
        
        category_list = Category.objects.all()
        
        context = {
            'category_list' : category_list
        }
        
        return render(request,self.template_name,context=context)
