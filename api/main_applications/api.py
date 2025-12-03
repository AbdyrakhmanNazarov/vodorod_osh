from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarApplicationSerializer  
from applications.models import CarApplication  
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def cars_list(request):
    # applications = CarApplication.objects.all()  
    # serializer = CarApplicationSerializer(applications, many=True)
    # return Response(serializer.data)

    application = CarApplication.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 3
    result_page = paginator.paginate_queryset(application, request)
    serializer = CarApplicationSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
def cars_create(request):
    serializer = CarApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def cars_detail(request, pk):
    try:
        application = CarApplication.objects.get(pk=pk)  
    except CarApplication.DoesNotExist:  
        return Response({"detail": "Not Found"}, status=404)
    
    if request.method == "GET":
        serializer = CarApplicationSerializer(application, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = CarApplicationSerializer(application, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        application.delete()
        return Response(status=204)