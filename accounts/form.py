from django.forms import ModelForm, PasswordInput

from accounts.models import AuthModel


class AuthRegisterForm(ModelForm):
    password = PasswordInput()
    class Meta:
        model = AuthModel
        fields = ["first_name","last_name","email","city"]

# now we will not use form because we need to modify some more text in html.
