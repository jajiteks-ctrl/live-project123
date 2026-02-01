from rest_framework import serializers

from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password"]

    
    def validate_username(self,value):
        if User.objects.filter(username = value).exists():
            raise serializers.ValidationError("User already exist")
        return value
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exist")
        return value
    
            
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        
   
   
from app.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email"]
        
   
   
from rest_framework import serializers
from app.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "products"]

