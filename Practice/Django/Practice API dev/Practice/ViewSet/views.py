from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import ViewsetModel
from .serializers import ViewsetmodelSerializer
from rest_framework.response import Response
from rest_framework import status
from .pagination import CustomPagination

# Create your views here.
class ViewSet(viewsets.ViewSet):
    pagination_class = CustomPagination

    def list(self, request):
        employee = ViewsetModel.objects.all()
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(employee, request)
        serializer = ViewsetmodelSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def create(self, request):
        serializer = ViewsetmodelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(ViewsetModel, pk=pk)
        serializer = ViewsetmodelSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def update(self, request, pk):
        employee= get_object_or_404(ViewsetModel, pk=pk)
        serializer = ViewsetmodelSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        employee = get_object_or_404(ViewsetModel, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_200_OK)