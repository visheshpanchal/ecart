from dataclasses import field

from django.contrib import admin

from .models import UserProfileAddress


# Register your models here.
class UserProfileAddressAdmin(admin.ModelAdmin):
    list_display = ("user_id","first_name","last_name","is_default")

admin.site.register(UserProfileAddress,UserProfileAddressAdmin)
