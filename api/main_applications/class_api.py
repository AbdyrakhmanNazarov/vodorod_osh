from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from applications.models import CarApplication, CarCategory
from .paginations import StandartResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
  CarCategorySerializer,
  #===================================
  CarApplicationsDetailSerializer,
  CarApplicationsListSerializer,
  CarApplicationsCreateUpdateSerializer
)
from .filters import CarFilter, CategoryFilter
from .permissions import PostPermission

class CarViewSet(ModelViewSet):
    queryset=CarApplication.objects.all()
    serializer_class = CarApplicationsListSerializer
    permission_classes = (PostPermission,)
    pagination_class = StandartResultsSetPagination
    filterset_class = CarFilter
    filter_backends = (DjangoFilterBackend, )
    # filterset_fields = ("car_brand", 
    #                     "car_model", 
    #                     "car_year", 
    #                     "engine_volume", 
    #                     "category",
    #                     "status", )

    # def get_serializer_class(self):
    #     if self.action == "retrieve":
    #         return CarApplicationsDetailSerializer
    #     elif self.action in ["create", "update", "partial_update"]:
    #         return CarApplicatiuonsCreateUpdateSerializer
    #     return super().get_serializer_class()
    
    # def get_permissions(self):
    #     if self.action in ["create", "update", "partial_update", "delete"]:
    #         return [IsAdminUser()]
    #     return super().get_permissions()
    

class CarCategoryViewSet(ModelViewSet):
    queryset=CarCategory.objects.all()
    serializer_class=CarCategorySerializer
    permission_classes = (PostPermission,)
    filterset_class = CategoryFilter
    filter_backends = (DjangoFilterBackend, )

    # def get_serializer_class(self):
    #     if self.action == "retrieve":
    #         return CarCategorySerializer
    #     elif self.action in ["create", "update", "partial_update"]:
    #         return CarCategorySerializer
    #     return super().get_serializer_class()
    
    # def get_permissions(self):
    #     if self.action in ["create", "update", "partial_update", "delete"]:
    #         return [IsAdminUser()]
    #     return super().get_permissions()
    