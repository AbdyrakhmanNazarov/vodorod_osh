from rest_framework import serializers
from applications.models import CarApplication, CarCategory

class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = "__all__"

#====================================================================
class CarApplicationsListSerializer(serializers.ModelSerializer):
    category = CarCategorySerializer(many=False)
    class Meta:
        model = CarApplication
        fields = ('id', 'user', 'car_brand', 'car_model', 'car_photo', 'category')

class CarApplicationsDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source= 'category.name', read_only=True)
    class Meta:
        model = CarApplication
        fields = "__all__"

class CarApplicationsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarApplication
        fields = "__all__"                