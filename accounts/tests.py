
import email

from django.contrib.auth import authenticate, get_user_model
from django.test import Client, TestCase

from accounts.models import AuthModel


class AccountTest(TestCase):
    
    def setUp(self) -> None:
        self.obj = AuthModel.objects.create_user(
            first_name = "Vishesh",
            last_name = "Panchal",
            email = "test@gmail.com",
            password = "1234567890"
        )
        
        self.obj.save()
    
        
    def test_account(self):
        user = AuthModel.objects.filter(first_name="Vishesh")
        self.assertEquals(user[0].first_name,"Vishesh")

        
class SignInTest(TestCase):
    
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name = "Vishesh",
            last_name = "Panchal",
            email = "test@gmail.com",
            password = "1234567890"
        )

    def tearDown(self) -> None:
        self.user.delete()
        
    
    def test_correct(self):
        user = authenticate(email="test@gmail.com",password="1234567890")
        
        self.assertTrue((user is not None) and user.is_authenticated)
