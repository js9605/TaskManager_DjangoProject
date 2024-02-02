from django.urls import path
from .views import register, custom_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
]
