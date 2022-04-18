
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from product.models import Product
from usr.models import UserProfileWishlist

from cart.models import CartModel

# Create your views here.

"""
[{
    product: product_query_set
    quantity : int,
    is_wishlisted : 'true' | ''  
},
{
    product: product_query_set
    quantity : int,
    is_wishlisted : 'true' | ''  
}]

"""


def is_wishlisted(product_id,category_id,user_id):
    user = UserProfileWishlist.objects.filter(user_id=user_id)
    if user :
        model = user[0].product_ids
        for ls in model['product_id']:
            if ls[0] == product_id and ls[1] == category_id:
                return "true"
    return ""



class Cart(View):
    def get(self,request):
        user_id = request.user.id
        
        user = CartModel.objects.filter(user_id=user_id)
        if user:
            
            query_list = list()
            
            
            obj = user[0].cart_items
            total = 0 # price toal
            quantity_total = 0
            for product in obj["products"]:
                product_dict = dict()
                product_id, category_id, quantity = product
                single_product = Product.objects.filter(product_id = product_id, category_id = category_id)
                if single_product:
                    ### Product Summery
                    total = total + int(single_product[0].product_price)
                    ### End Product Summery 
                    quantity_total = quantity_total + quantity
                    
                    product_dict["product"] = single_product[0]
                    product_dict["quantity"] = quantity
                    product_dict["is_wishlisted"] = is_wishlisted(product_id,category_id,user_id=user_id)
   
                
                query_list.append(product_dict)
                
            discount = total * 0.02
            
            
            context_data = {
                "products":query_list,
                "total" : total,
                "discount" : discount,
                "quantity" : quantity_total
            }
        return render(request,"user_cart.html",context=context_data)


class AddCart(View):
    def get(self,request,category,product):
        user = request.user.id
        
        user_model = CartModel.objects.filter(user_id=user)
        if user_model:
            product_dict = user_model[0].cart_items
            
            temp_list = product_dict["products"]
            temp_list.append([product,category,1])
            
            ## Saving Object
            data = dict()
            data["products"] =  temp_list
            user_model[0].cart_items = data
            user_model[0].save()
        
        return redirect(reverse("category:product_details")+"?product_id={0}".format(product))
    
    
    
class RemoveCart(View):
    def get(self,request,category,product):
        user = request.user.id
        
        user_model = CartModel.objects.filter(user_id=user)
        if user_model:
            product_dict = user_model[0].cart_items
            
            temp_list = product_dict["products"]
            for i in temp_list:
                if i[0] == product and i[1] == category:
                    temp_list.remove([product,category,i[2]])
                    break
            
            ## Saving Object for Remove Cart:
            data = dict()
            data["products"] = temp_list
            user_model[0].cart_items = data
            user_model[0].save()
        return redirect(request.META.get("HTTP_REFERER"))

@login_required(login_url="accounts:account_login")
def increment(request,category,product):
    user_id = request.user.id
    
    user_model = CartModel.objects.filter(user_id=user_id)
    if user_model:
        product_dict = user_model[0].cart_items
        
        temp_list = product_dict["products"]
        for i in temp_list:
            if i[0] == product and i[1] == category:
                temp_list.remove([product,category,i[2]])
                quantity = int(i[2])
                data = [product,category, quantity + 1]
                temp_list.append(data)
                break
        ## Saving Object for increment cart:
        data = dict()
        data["products"] = temp_list
        user_model[0].cart_items = data
        user_model[0].save()
    
   
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url="accounts:account_login")
def decrement(request,category,product):
    user_id = request.user.id
    
    user_model = CartModel.objects.filter(user_id=user_id)
    if user_model:
        product_dict = user_model[0].cart_items
        
        temp_list = product_dict["products"]
        for i in temp_list:
            if i[0] == product and i[1] == category:
                temp_list.remove([product,category,i[2]])
                quantity = int(i[2])
                if quantity == 1:
                    return redirect("cart:remove_cart",product=product,category=category)
                dt = [product,category, quantity - 1]
                temp_list.append(dt)
                break
            

        ## Saving Object for increment cart:
        data = dict()
        data["products"] = temp_list
        user_model[0].cart_items = data
        user_model[0].save()
    return redirect(request.META.get('HTTP_REFERER', '/'))
