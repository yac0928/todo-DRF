from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="Test description"
    ),
    public=True,
)

urlpatterns = [
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
    path('auth/', include('rest_framework.urls')),
    path('api/jwtauth/', include('jwtauth.urls'), name='jwtauth'),
]
