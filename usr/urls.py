from django.urls import path

from usr.add_views import (user_add_address, user_address, user_address_delete,
                           user_wishlist)

from .views import user_order, user_profile, user_seller, user_settings

app_name = "profile"
urlpatterns = [
    path("main/",user_profile,name="main"),
    path("address/",user_address,name="address"),
    path("address/add/",user_add_address,name="add_address"),
    path("address/delete/",user_address_delete,name="delete_address"),
    path("orders/",user_order,name="order"),
    path("seller/",user_seller,name="seller"),
    path("settings/",user_settings,name="settings"),
    path("wishlist/",user_wishlist,name="wishlist"),
]
