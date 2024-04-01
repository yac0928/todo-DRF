from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Todo, Location
from .serializers import LocationSerializer, TodoReadSerializer, TodoWriteSerializer
from rest_framework.exceptions import PermissionDenied

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class TodoViewSet(ModelViewSet):
    permission_classes = (IsAuthor,)
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Todo.objects.filter(author=user)
        raise PermissionDenied()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TodoReadSerializer
        else:
            return TodoWriteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer