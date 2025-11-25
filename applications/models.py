from django.db import models
from accounts.models import User

class CarApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    
    car_brand = models.CharField(max_length=100, verbose_name="Марка машины")
    car_model = models.CharField(max_length=100, verbose_name="Модель машины")
    car_year = models.PositiveIntegerField(verbose_name="Год выпуска")
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Объем двигателя (л)")
    car_photo = models.ImageField(
        upload_to='car_photos/%Y/%m/%d/',  # ИСПРАВЛЕН ПУТЬ
        verbose_name="Фото машины", 
        blank=True, 
        null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    
    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Заявка на авто"
        verbose_name_plural = "Заявки на авто"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.car_brand} {self.car_model} ({self.car_year}) - {self.user.email}"