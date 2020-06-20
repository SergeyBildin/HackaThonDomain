from django.shortcuts import render
from django.views.generic import CreateView, View, FormView
from .models import Account
from.forms import RegisterForm

class RegistrationView(FormView):
    model = Account
    template_name = 'Registration.html'
    form_class = RegisterForm
    success_message = 'Пользователь успешно создан'
    #skills = analysis_user(get_user_id(Account.objects.get(email=self.request.user.email)),)
    success_url = '/secondReg/'
    def form_valid(self,form):
        form.save()
