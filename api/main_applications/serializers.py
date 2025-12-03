from rest_framework import serializers
from applications.models import CarApplication  
from accounts.models import User

class CarApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarApplication
        fields = "__all__"
