from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager

class User(AbstractUser, PermissionsMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-date_joined",)  
        
    username = None
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    phone_number = PhoneNumberField(verbose_name="Номер телефона", blank=True, null=True)
    full_name = models.CharField(max_length=200, verbose_name="ФИО") 

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """Возвращает полное имя"""
        return self.full_name
    
    def __str__(self):
        return self.email or self.full_name