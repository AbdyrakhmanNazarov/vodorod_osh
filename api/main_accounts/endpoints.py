from django.urls import path
from .api import users_list, users_create, users_detail

urlpatterns = [
    path('', users_list, name='users-list'),           
    path('create/', users_create, name='users-create'), 
    path('<int:pk>/', users_detail, name='users-detail'), 
]
