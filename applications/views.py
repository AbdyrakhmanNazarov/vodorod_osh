from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CarApplication
from .forms import CarApplicationForm
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import CarApplication

def our_clients(request):
    approved_applications = CarApplication.objects.filter(
        status='approved'
    ).order_by('-created_at')
    
    paginator = Paginator(approved_applications, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'our_clients.html', {
        'page_obj': page_obj,
        'applications': page_obj.object_list,
    })

@login_required
def user_dashboard(request):
    user_applications = CarApplication.objects.filter(user=request.user)
    return render(request, 'user/user_dashboard.html', {
        'applications': user_applications
    })

@login_required
def create_application(request):
    if request.method == 'POST':
        form = CarApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, "Заявка успешно создана!")
            return redirect('user_dashboard')
    else:
        form = CarApplicationForm()
    
    return render(request, 'user/user_create.html', {'form': form})

@login_required
def update_application(request, pk):
    application = get_object_or_404(CarApplication, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = CarApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно обновлена!")
            return redirect('user_dashboard')
    else:
        form = CarApplicationForm(instance=application)
    
    return render(request, 'user/user_update.html', {'form': form})

@login_required
def delete_application(request, pk):
    application = get_object_or_404(CarApplication, pk=pk, user=request.user)
    
    if request.method == 'POST':
        application.delete()
        messages.success(request, "Заявка успешно удалена!")
        return redirect('user_dashboard')
    
    return render(request, 'user/user_confirm_delete.html', {'application': application})