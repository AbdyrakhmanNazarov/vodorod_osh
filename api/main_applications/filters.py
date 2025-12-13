from django_filters import FilterSet, NumberFilter, ChoiceFilter, CharFilter, ModelChoiceFilter
from applications.models import CarApplication, CarCategory

class CarFilter(FilterSet):
    car_brand = CharFilter(field_name='car_brand', lookup_expr='exact')

    car_model = CharFilter(field_name='car_model', lookup_expr='exact')

    car_year_exact = NumberFilter(field_name='car_year', lookup_expr='exact')
    car_year_min = NumberFilter(field_name='car_year', lookup_expr='gte')
    car_year_max = NumberFilter(field_name='car_year', lookup_expr='lte')

    engine_volume_exact = NumberFilter(field_name='engine_volume', lookup_expr='exact')
    engine_volume_min = NumberFilter(field_name='engine_volume', lookup_expr='gte')
    engine_volume_max = NumberFilter(field_name='engine_volume', lookup_expr='lte')


    category = ModelChoiceFilter(field_name='category', queryset=CarCategory.objects.all())

    class Meta:
        model = CarApplication
        fields = []


class CategoryFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='exact')

    class Meta:
        model = CarCategory
        fields = []