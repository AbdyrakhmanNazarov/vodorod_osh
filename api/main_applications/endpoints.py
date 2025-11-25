from django.urls import path
from .api import cars_list, cars_create, cars_detail 

urlpatterns = [
    path('cars/', cars_list, name='cars-list'),
    path('cars/create/', cars_create, name='cars-create'),
    path('cars/<int:pk>/', cars_detail, name='cars-detail'),
]