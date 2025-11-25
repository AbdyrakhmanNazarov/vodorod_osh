from django.urls import path
from .views import login_custom, register_view, logout_view, about_view, contacts_view, our_clients_view, user_dashboard

urlpatterns = [
    path("login/", login_custom, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("about/", about_view, name="about"),     
    path("contacts/", contacts_view, name="contacts"), 
    path("our-clients/", our_clients_view, name="our_clients"), 
    path("dashboard/", user_dashboard, name="user_dashboard"),   
]