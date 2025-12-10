from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from applications.models import CarApplication, CarCategory
from .serializers import (
  CarCategorySerializer,
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

class CarCategoryViewSet(ReadOnlyModelViewSet):
    queryset=CarCategory.objects.all()
    serializer_class=CarCategorySerializer


