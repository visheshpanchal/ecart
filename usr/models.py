from django.db import models

# Create your models here.
# class AccountMain(models):
#     user_id = models.IntegerField(default=0)

# New Model Idea
# We add user_id in each models of usr,
# We add AuthModel id in accounts.
# When we use dual database then we can access using AuthModel's Primary key(i.e. ID)


class UserProfileAddress(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    email = models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_number = models.CharField(max_length=6)
    address_1 = models.CharField(null=False,max_length=256)
    address_2 = models.CharField(null=False,max_length=256)
    is_default = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = "ProfileAddress"

    def __str__(self) -> str:
        return str(self.user_id) + " " + self.first_name



### Wishlist Structure
    """        structure :
        user_id : int
        product_ids :{ product_id :  [ [product_id, category_id],
                        [product_id, category_id],
                    ]}

    Returns:
        _type_: _description_
    """
class UserProfileWishlist(models.Model):
    user_id = models.IntegerField(unique=True)
    product_ids = models.JSONField()

    def __str__(self) -> str:
        return str(self.user_id)
