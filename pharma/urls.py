from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from precscription import views
from rest_framework.authtoken.views import obtain_auth_token 
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger for api-doc.
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'precscription', views.PrecscriptionViewSet, basename="precscription")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api-doc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-api-doc'),
    path("api/", include((router.urls, "precscription"),  namespace='api')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

