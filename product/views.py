
from django.http import HttpRequest, QueryDict
from django.shortcuts import render
from django.views import View

from .models import Category, Product


# Create your views here.
class CategoryView(View):
    
    def get(self,request,pk=None):
        if pk == None:
            
            categories = Category.objects.all()
        else:
            
            categories = Category.objects.filter(category_id=pk)
            
        context = {
            "categories":categories,
        }
        
        return render(request,'./category.html',context)

class ProductView(View):
    
    def query(self,request:HttpRequest) -> dict: 
        if request.method == "GET":
            query_dict = QueryDict(request.META['QUERY_STRING'])
            return query_dict.dict()
        else:
            return dict() 
    
    
    def get(self,request:HttpRequest,pk=None):
        query_dict = self.query(request)
        
        args = dict()
        if bool(query_dict):
            for k,v in query_dict.items():
                    args[k] = v
            
        if pk == None:
            product = Product.objects.all().filter(**args)
        else :
            product = Product.objects.filter(product_id=pk)
        context = {
            "products":product
        }
        
        return render(request,'product-list.html',context=context)


class ProductDetail(View):
    
    def query(self,request:HttpRequest) -> dict: 
        if request.method == "GET":
            query_dict = QueryDict(request.META['QUERY_STRING'])
            return query_dict.dict()
        else:
            return dict() 
    
    
    def get(self,request):
        query_dict = self.query(request)
        
        args = dict()
        if bool(query_dict):
            for k,v in query_dict.items():
                args[k] = v
        
        
        return render(request,"detail-product.html")
