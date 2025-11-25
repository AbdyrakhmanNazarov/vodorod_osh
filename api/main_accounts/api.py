from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from accounts.models import User

@api_view(['GET'])
def users_list(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def users_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"detail":"Not Fount"})
    
    if request.method == "GET":
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = UserSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        user.delete()
        return Response(status=204)
