from django.urls import path
from .api import custom_login, custom_register, custom_logout, profile, change_password 

urlpatterns = [
    path('login/', custom_login, name = 'login'),
    path('register/', custom_register, name = 'register'),
    path('logout/', custom_logout, name = 'logout'),
    path('profile/', profile, name = 'profile'),
    path('change_password/', change_password, name = 'change_password'),
]