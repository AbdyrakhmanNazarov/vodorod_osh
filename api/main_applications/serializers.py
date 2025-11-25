from rest_framework import serializers
from applications.models import CarApplication  

class CarApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarApplication
        fields = ('id', 'user', 'car_brand', 'car_model', 'car_year', 'engine_volume', 'car_photo', 'description', 'status', 'created_at')  