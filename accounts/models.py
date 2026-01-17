from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager
from django.utils.timezone import now

class User(AbstractUser, PermissionsMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-date_joined",)  
        
    username = None
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    phone_number = PhoneNumberField(verbose_name="Номер телефона", blank=True, null=True)
    full_name = models.CharField(max_length=200, verbose_name="ФИО") 
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """Возвращает полное имя"""
        return self.full_name
    
    def __str__(self):
        return self.email or self.full_name
    

class OTPVerification(models.Model):
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def is_expired(self):
        return (now() - self.created_at).seconds > 300
    
    def __str__(self):
        return f"{self.email} - {self.code}"