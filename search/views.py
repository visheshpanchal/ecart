

from django.db.models import Q
from django.http import HttpRequest, QueryDict
from django.shortcuts import render
from numpy import product
from product.models import Category, Product


def query(request:HttpRequest) -> dict:
    if request.method == "GET":
        query_dict = QueryDict(request.META['QUERY_STRING'])
    else:
        query_dict = dict()
    return query_dict



def search_category(search_text,type_name):
    model = Category.objects
    
    if search_text == "" and type_name in ("all","product"):
        data = model.all()
        return data
        
    if type_name in ("all","category"):
        data = model.filter(Q(category_name__contains=search_text) | Q(category_description__contains=search_text))
        return data
    
    return []


def search_product(search_text,type_name):
    model = Product.objects
    if search_text == "" and type_name in ("all","product"):
        data = model.all()
        return data
    
    if type_name in ("all","product"):
        data = model.filter(Q(product_name__contains=search_text) | Q(product_details__contains=search_text))    
        return data
    
    return []

def search(request):
    query_dict = query(request)
    
    search_text = query_dict['search']
    type_name = query_dict['category_name']
    
    category_data = search_category(search_text,type_name)
    product_data = search_product(search_text,type_name)
    
    context_data = {
        "category" : category_data,
        "product" : product_data
    }
    print(search_text,"----------- search text")
    
    return render(request,"search.html",context=context_data)
