

from accounts.models import AuthModel
from cart.models import CartModel
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

from usr.models import UserProfileAddress, UserProfileWishlist


# Create your views here.
@login_required(login_url="accounts:account_login")
def user_profile(request:HttpRequest):
    user_id = request.user.id
    
    user_data = AuthModel.objects.filter(pk=user_id)
    
    user_address = UserProfileAddress.objects.filter(user_id=user_id)
    
    
    
    return render(request,"profile_user/main.html",context={"user_data":user_data,"user_address":user_address})
















@login_required(login_url="accounts:account_login")
def user_order(request):
    
    return render(request,"profile_user/orders.html")

@login_required(login_url="accounts:account_login")
def user_wishlist(request):
    
    return render(request,"profile_user/wishlist.html")

@login_required(login_url="accounts:account_login")
def user_settings(request):
    # This will store current user's primary key (id)
    user_id = request.user.id 
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        country = request.POST['country']
        city = request.POST['city']
        zip_no = request.POST['zip']
        phone_no = request.POST['phone']
        
        if str(country) == 'Choose...':
            country = 'None'

        
    return render(request,"profile_user/setting.html")


@login_required(login_url="accounts:account_login")
def user_seller(request):
    return render(request,"profile_user/seller.html")


