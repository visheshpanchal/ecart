from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import AuthModel

# Register your models here.

User = get_user_model()


class UserAuthAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','last_login')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login',)
    
    ordering = ('-last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User,UserAuthAdmin)
