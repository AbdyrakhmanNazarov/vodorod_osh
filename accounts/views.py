from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import User

def about_view(request):
    return render(request, "about.html")

def contacts_view(request):
    return render(request, "contacts.html")

def main_view(request):
    return render(request, "main.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        full_name = request.POST.get("full_name")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Пароли не совпадают")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Пользователь с таким email уже существует.")
            return redirect('register')

        User.objects.create_user(email=email, password=password, full_name=full_name)
        messages.success(request, "Регистрация прошла успешно! Войдите в систему.")
        return redirect("login")

    return render(request, "auth/register.html")

def login_custom(request):
    if request.user.is_authenticated:
        return redirect("main")
    
    if request.method == "POST":
        email = request.POST.get("email")  
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect("main")
        else:
            messages.error(request, "Неверный email или пароль, либо аккаунт неактивен")

    return render(request, "auth/login.html")



def our_clients_view(request):
    return render(request, "our_clients.html")

def user_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "user_dashboard.html")