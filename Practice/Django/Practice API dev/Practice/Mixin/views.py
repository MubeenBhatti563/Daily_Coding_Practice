from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Cities
from .serializers import CitySerializer

# Create your views here.
"""
class CityView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class CityDetailView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
""" 

class CityGenericView(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer

class CityGenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'pk'