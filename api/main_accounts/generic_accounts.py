from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser)
from accounts.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import (
    RegisterSerializer, 
    ProfileSerializer,
    LoginSerializer,
    ActivateSerializer,
    DeactivateSerializer,
    GenericChangePasswordSerializer
)

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class ProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        return self.request.user
    

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    
class ChangePasswordView(GenericAPIView):
    serializer_class = GenericChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        
        # Проверка старого пароля
        user = request.user
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')
        
        if not user.check_password(old_password):
            return Response(
                {"error": "Старый пароль неверен"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Установка нового пароля
        user.set_password(new_password)
        user.save()
        
        # Удаление токена для безопасности
        Token.objects.filter(user=user).delete()
        
        return Response({"message": "Пароль успешно изменен"})
    
class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({"message":"Вы вышли из системы"})    
    
class DeactivateAccountView(GenericAPIView):
    serializer_class = DeactivateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not serializer.validated_data['confirm']:
            return Response({"error":"Подтвердите деактивацию"})
        
        request.user.is_active=False
        request.user.save()

        return Response({"message":"Аккаунт деактивирован"}) 
