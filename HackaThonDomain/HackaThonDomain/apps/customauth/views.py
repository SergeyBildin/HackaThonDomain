from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from .models import Account
from .forms import RegisterForm, AuthForm
from .UAInterface import checkEmail


class RegistrationView(FormView):
    model = Account
    template_name = 'Registration.html'
    form_class = RegisterForm
    success_message = 'Пользователь успешно создан'    
    
    #success_url = '/secondReg/'    
    def form_valid(self,form):
        if checkEmail(form.email):
            form.save()        
            email = self.request.POST['email']
            password = self.request.POST['password1']        
            user = authenticate(email=email, password=password)
            print('User:', user)
            login(self.request, user)
            return super(RegistrationView,self).form_valid(form)

class AuthView(LoginView):
    template_name = 'Authorization.html'
    form_class = AuthForm
    #success_url =
    def get_success_url(self):
        return self.success_url