from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
        #path('',views.main, name = 'welcome'),
        path('Registration/', views.RegistrationView.as_view(), name = 'Registration'),
        #path('secondReg/', views.ProfileCreateView.as_view(), name = 'secondReg'),
        path('login/', views.AuthView.as_view(), name = 'login'),
        #path('logout', views.Logout.as_view(), name = 'logout'),
        
]