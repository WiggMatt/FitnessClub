from django.contrib import admin
from django.urls import path

from main_app import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view,  name='logout'),
]
