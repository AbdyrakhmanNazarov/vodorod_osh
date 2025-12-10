from rest_framework.routers import DefaultRouter
from .class_api import CarViewSet, CarCategoryViewSet
from django.urls import path, include

router=DefaultRouter()
router.register('car-applications', CarViewSet, basename='car-applications')
router.register('car-category', CarCategoryViewSet, basename='car-category')

urlpatterns = [
    path('', include(router.urls))
]   