from django.contrib import admin
from .models import CarApplication, CarCategory

@admin.register(CarApplication)
class CarApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car_brand', 'car_model', 'car_year', 'status', 'created_at')
    list_display_links = ('id', 'car_brand')
    list_filter = ('status', 'car_year', 'created_at')
    search_fields = ('car_brand', 'car_model', 'user__email', 'user__full_name')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 20
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'status')
        }),
        ('Информация об автомобиле', {
            'fields': ('car_brand', 'car_model', 'car_year', 'engine_volume', 'car_photo', 'description')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    