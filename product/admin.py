from django.contrib import admin

from .models import Category, Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    exclude = ("product_width","product_height")

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
