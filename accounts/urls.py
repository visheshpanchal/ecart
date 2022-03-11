from django.urls import path

from .views import AccountLogin, AccountRegister, Logout

app_name="accounts"
urlpatterns = [
    path("register/",AccountRegister.as_view(),name="account_register"),
    path("login/",AccountLogin.as_view(),name="account_login"),
    path("logout/",Logout.as_view(),name='account_logout')
]
