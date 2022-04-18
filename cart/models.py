from django.db import models



# Create your models here.
class CartModel(models.Model):
    user_id = models.IntegerField(null=True)
    cart_items = models.JSONField(null=True)
