from django.contrib.auth.decorators import login_required
from django.urls import path

from cart.views import AddCart, Cart, RemoveCart, decrement, increment

app_name = "cart"
urlpatterns = [
    path("",login_required(Cart.as_view(),login_url="accounts:account_login"),name="user_cart"),
    path("add/<int:category>/<int:product>/",login_required(AddCart.as_view(),login_url="accounts:account_login"),name="add_cart"),
    path("remove/<int:category>/<int:product>/",login_required(RemoveCart.as_view(),login_url="accounts:account_login"),name="remove_cart"),
    path("increment/<int:category>/<int:product>/",increment,name="increment"),
    path("decrement/<int:category>/<int:product>/",decrement,name="decrement")
]
