from rest_framework import serializers
from applications.models import CarApplication, CarCategory
from accounts.models import User

class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = "__all__"

class CarApplicationsListSerializer(serializers.ModelSerializer):
    car_category = CarCategorySerializer(many=False)
    class Meta:
        model = CarApplication
        fields = ('id', 'user', 'car_brand', 'car_model', 'car_photo', 'car_category')


class CarApplicationsDetailSerializer(serializers.ModelSerializer):
    carcategory_name = serializers.CharField(source= 'car_category.object.name', read_only=True)
    class Meta:
        model = CarApplication
        fields = "__all__"

class CarApplicatiuonsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarApplication
        fields = "__all__"                