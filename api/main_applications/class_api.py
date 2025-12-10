from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from applications.models import CarApplication, CarCategory
from .serializers import (
  CarCategoryListSerializer,
  CarCategoryDetailSerializer,
  CarCategoryCreateUpdateSerializer,
  #===================================
  CarApplicationsDetailSerializer,
  CarApplicationsListSerializer,
  CarApplicatiuonsCreateUpdateSerializer
)




class CarViewSet(ModelViewSet):
    queryset=CarApplication.objects.all()
    serializer_class = CarApplicationsListSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CarApplicationsDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return CarApplicatiuonsCreateUpdateSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()
    



class CarCategoryViewSet(ModelViewSet):
    queryset=CarCategory.objects.all()
    serializer_class=CarCategoryListSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CarCategoryDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return CarCategoryCreateUpdateSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAdminUser()]
        return super().get_permissions()