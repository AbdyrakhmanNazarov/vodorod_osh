from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('create/', views.create_application, name='create_application'),
    path('update/<int:pk>/', views.update_application, name='update_application'),
    path('delete/<int:pk>/', views.delete_application, name='delete_application'),
    path('our-clients/', views.our_clients, name='our_clients'),
]