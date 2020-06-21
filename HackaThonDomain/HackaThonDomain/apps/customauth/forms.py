from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account



class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

class AuthForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = Account
        exclude = ('email','is_staff','is_active','is_superuser', 'is_admin')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"