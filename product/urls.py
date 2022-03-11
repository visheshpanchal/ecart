from django.urls import path, re_path

from .views import CategoryView, ProductDetail, ProductView

app_name = "category"
urlpatterns = [
    path('',CategoryView.as_view(),name="all"),
    path('products/',ProductView.as_view(),name="product_all"),
    path('<slug:pk>/',CategoryView.as_view(),name="few"),
    path('products/<int:pk>',ProductView.as_view(),name="product_id"),
    
    # single page product details
    path('products/detail/',ProductDetail.as_view(),name="product_details")
    
]
