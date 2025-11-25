from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import main_view 

urlpatterns = [
    path("", main_view, name="main"),  
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')),  
    path("accounts/", include("accounts.urls")), 
    path("applications/", include("applications.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)