from django.urls import path, include

urlpatterns = [
    path('', include('api.yasg')),
    path('accounts/', include('api.main_accounts.endpoints')),  
    path('applications/', include('api.main_applications.endpoints')),  
]
