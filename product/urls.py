from django.urls import path, re_path

from .views import (CategoryView, ProductDetail, ProductView, WishlistAdd,
                    WishlistRemove)

app_name = "category"
urlpatterns = [
    path('',CategoryView.as_view(),name="all"),
    
    # i.e /category/product/?category_id=id
    path('products/',ProductView.as_view(),name="product_all"),
    
    # i.e category/category_id/
    path('<slug:pk>/',CategoryView.as_view(),name="few"),
    
    
    path('products/<int:pk>',ProductView.as_view(),name="product_id"),
    
    # single page product details
    ## i.e /category/products/detail/?product_id=1&category_id=1
    path('products/detail/',ProductDetail.as_view(),name="product_details"),
    path('product/wishlist/add/<int:product_id>/<int:category_id>/',WishlistAdd.as_view(),name="product_add"),
    path('product/wishlist/remove/<int:product_id>/<int:category_id>/',WishlistRemove.as_view(),name="product_remove")
    
]
