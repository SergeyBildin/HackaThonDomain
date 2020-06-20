from django import forms
from .validate import validate_email
from django.forms.fields import EmailField
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class MyEmailField(EmailField):
    default_validators = [validate_email]

class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email',)
        fields_classes = { 'email' : MyEmailField }