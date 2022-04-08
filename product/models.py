
from typing import Iterable, Optional

from django.db import models
from django.urls import reverse
from PIL import Image

# Create your models here.
CATEGORY_CHOICE = [
    ("cloth","Cloth"),
    ("food","Food"),
    ("fashion","Fashion"),
    ("book","Book"),
    ("baby product","Baby Products"),
    ("jewelry","Jewelry")
]

## For category model use id field as identification
class Category(models.Model):
    category_id = models.IntegerField(unique=True)
    category_description = models.TextField(default="")
    category_name = models.CharField(max_length=15,choices=CATEGORY_CHOICE,default='food')
    category_image = models.ImageField(default="",upload_to="app_static/images")
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.category_name
    
    def get_url(self):
        return reverse("category:product_all",args=["{0}".format(self.id)])


## For Product_id model use product_id as identifier
class Product(models.Model):
    
    product_id = models.IntegerField(unique=True)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=64)
    product_quantity = models.IntegerField()
    product_details = models.TextField()
    product_image = models.ImageField()
    product_width = models.CharField(max_length=24,default="")
    product_height = models.CharField(max_length=24,default="")
    product_time = models.DateField(auto_now_add=True)
    product_price = models.IntegerField(default=0)
    

    def __str__(self):
        return self.product_name

    def save(self,*args,**kwargs):
        img = Image.open(self.product_image)
        width, height = img.size
        self.product_width = (str(width))
        self.product_height = (str(height))
        return super(Product,self).save(*args,**kwargs)


    
# Product Image Specification
class ProductImageDimensions(models.Model):
    # We need add product id bcz we are not using foreign key
    product_id = models.IntegerField(unique=True)
    width = models.IntegerField(default=0)
    hight = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    
    
class ProductExtraDetails(models.Model):
    # We need add product id bcz we are not using foreign key
    product_id = models.IntegerField(unique=True)
    
