from datetime import datetime
from operator import contains
from random import choice

from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateResponseMixin, View
from product.models import Category, Product


### Adding Random Product For Displaying ###
def rproduct(k=3):
    """ k : total number of random items return. """
    obj = Product.objects.all()
    if len(obj) <= k :
        return obj
    ls = list()
    while len(ls) != k:
        a = choice(obj)
        if not contains(ls,a):
            ls.append(a)
    
    return ls

def rcategory(k=3):
    """ prove k random category from data base """
    obj = Category.objects.all()
    if len(obj) < k:
        return obj
    ls = list()
    while len(ls) != k:
        a = choice(obj)
        if not contains(ls,a):
            ls.append(a)
    return ls
    

def get_timer_deal(request:HttpResponse):
    time_now = datetime.now()
    
    sale_time = datetime(time_now.year,time_now.month,time_now.day,hour = 23,minute = 59,second = 59)
    
    time_delta = sale_time - time_now
    
    return (time_delta.seconds)


def deal_products():
    return rproduct(k=5)


def get_section_category(k=2):
    """ 
    return category_list with k values and product_list value depend on category_list
    """
    
    cat_ls = list()
    obj_category = Category.objects.all()
    
    if len(obj_category) <= k:
        return obj_category
    
    while len(cat_ls) != k:
        a = choice(obj_category)
        if not contains(cat_ls,a):
            cat_ls.append(a)
    
    pro_ls = list()
    cat_id = [ i.id for i in cat_ls]
    obj_product = Product.objects.all()
    """ check for product """
    if len(obj_product) < k :
        return obj_product
    
    for i in obj_product:
        if i.category_id.id in cat_id:
            pro_ls.append(i)
    
    
    return cat_ls, pro_ls 
        

## Our Home Page
class Home(View,TemplateResponseMixin):
    template_name = "./home.html"
    
    def get(self,request:HttpRequest):
        
        category_list = Category.objects.all()
        
        ### Adding Radnom List ###
        random_product = rproduct(3)
        random_category = rcategory()
        get_timer = get_timer_deal(request)
        get_deal_product = deal_products()
        section_category, section_product = get_section_category()
        context = {
            'category_list' : category_list,
            'rproducts' : random_product,
            'rcategory' : random_category,
            "timer" : get_timer,
            "is_timer" : "true",
            'get_deal_product' : get_deal_product,
            "section_category" : section_category,
            "section_product" : section_product,
            "recommanded_items" : rproduct(k=16)
        }
        
        
        print(random_product)
        
        return render(request,self.template_name,context=context)

