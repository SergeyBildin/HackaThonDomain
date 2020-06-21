from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
        path('',views.index, name = 'welcome'),
        path('Registration/', views.RegistrationView.as_view(), name = 'Registration'),
        path('SuccessReg/', views.success_reg, name = 'success_reg'),
        path('login/', views.AuthView.as_view(), name = 'login'),
        #path('l', views.Logout.as_view(), name = 'logout'),
        
]