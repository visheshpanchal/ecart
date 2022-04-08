
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, resolve_url
from django.urls import resolve
from product.models import Product
from usr.models import UserProfileWishlist


@login_required(login_url="accounts:account_login")
def user_wishlist(request):
    user_id = request.user.id
    
    obj = UserProfileWishlist.objects.filter(user_id=user_id)
    products_id_ls = obj[0].product_ids['product_id']
    
    ls = list()
    for i in products_id_ls:
        product = Product.objects.get(product_id=i[0])
        ls.append(product)
    
    product = {"products":ls}
        
    
    return render(request,"profile_user/wishlist.html",context=product)
