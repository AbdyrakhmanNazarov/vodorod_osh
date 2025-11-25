from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        ffields = ('id', 'email', 'phone_number', 'full_name', 'is_staff', 'is_active', 'date_joined')