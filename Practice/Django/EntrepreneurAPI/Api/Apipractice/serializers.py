from rest_framework import serializers
from rest_framework.reverse import reverse
from .related_serializers import UsernameSerializer
from .validators import validate_name, validate_no_hello
from .models import Customer, Student, Employee, Manager, Product

class CustomerSerializer(serializers.ModelSerializer):
    """
    Docstring for CustomerSerializer
    """
    class Meta:
        model = Customer
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    """
    Docstring for StudentSerializer
    """
    class Meta:
        model = Student
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Docstring for EmployeeSerializer
    """
    class Meta:
        model = Employee
        fields = "__all__"

class UsernameProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'products',
        lookup_field = 'pk',
        read_only = True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    """
    Docstring for ProductSerializer
    """
    url = serializers.SerializerMethodField(read_only=True)
    # owner = UsernameSerializer(source='user', read_only=True)
    # username = serializers.SerializerMethodField(read_only=True)
    # related_products = UsernameProductInlineSerializer(source='user.products.all', read_only=True, many=True)
    class Meta:
        model = Product
        fields = [
            'user',
            # 'related_products',
            'url',
            'id',
            'title',
            'content',
            'price',
            # 'username'
        ]
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("products", kwargs={'pk': obj.pk}, request=request)
        # return f"api-auth/product/{obj.pk}/"

class ManagerSerializer(serializers.ModelSerializer):
    """
    Docstring for ManageSeializer
    """
    url = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validate_name, validate_no_hello])
    # title = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = Manager
        fields = [
            "url",
            "email",
            "pk",
            "name",
            # 'title',
            "manage",
            "age"
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("manager-detail", kwargs={"pk": obj.pk}, request=request)
    
    def create(self, instance, validated_data):
        email = validated_data.pop("email", None)
        if email:
            print(f"Sending notification to {email}")
        return super().update(instance, validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)