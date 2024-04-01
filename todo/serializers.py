from rest_framework import serializers
from .models import Todo, User, Location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TodoReadSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    location = LocationSerializer(read_only=True)
    class Meta:
        model = Todo
        fields = '__all__'

class TodoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        extra_kwargs = {"author": {"read_only": True}}