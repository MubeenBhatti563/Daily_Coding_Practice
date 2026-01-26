from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, mixins, status, permissions, authentication
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Customer, Student, Employee, Manager
from .serializers import CustomerSerializer, StudentSerializer, EmployeeSerializer, ManagerSerializer
from .authorization import TokenAuthentication
from .mixins import StaffEditorPermissionMixin
# Create your views here.
# Functions based Views
@api_view(['GET', 'POST'])
def home_api(request):
    """
    Docstring for home_api
    
    :param request: Request coming from ClientSide
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT', 'GET', 'DELETE'])
def get_customer(request, pk):
    """
    Docstring for get_customer
    
    :param request: request coming from clinet side
    :param pk: Individual object of model
    """
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_200_OK)

# Class based views
class StudentView(APIView):
    """
    Student view APIs for Client
    """
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication
    # ]

    def get(self, request, *args, **kwargs):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class StudentViewSingle(APIView):
    """
    APIs for Individual students
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    def get(self, request, pk, *args, **kwargs):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, *args, **kwargs):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_200_OK)
    
# Mixins
class EmployeeView(
    StaffEditorPermissionMixin,
    mixins.CreateModelMixin, 
    mixins.ListModelMixin, 
    generics.GenericAPIView
    ):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request)
    
class EmployeeViewSingle(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
    ):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk)
    
    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk)
    
    def delete(self, request, pk, *args, **kwargs):
        return self.delete(request, pk)
    
# Generics Views
class ManagerView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        manage = serializer.validated_data.get('manage')
        if manage is None:
            manage = name
        serializer.save(manage=manage)

class ManagerViewSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    lookup_field = 'pk'