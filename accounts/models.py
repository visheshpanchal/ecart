from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

## Custom User Model

class AuthModelManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,password):
        
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
        )
        
        user.set_password(password)
        # save pass word using=self._db means default database config.
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,email,password):
        if email == None:
            raise ValueError("User must have an email address")
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
            password=password
        )
        
        #user.is_admin = True
        user.is_admin = True
        user.is_superuser = True
        
        
        # save pass word using=self._db means default database config.
        user.save(using=self._db)
        return user
        
class AuthModel(AbstractBaseUser):
    
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(verbose_name="Email Address",unique=True,max_length=255)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
   
    
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']
    class Meta:
        verbose_name = "Auth"
        
        
    objects = AuthModelManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
 
