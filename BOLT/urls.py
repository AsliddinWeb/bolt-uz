from django.contrib import admin
from django.urls import path, include

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Static settings
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.authentication import JWTAuthentication

# JWT Auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# getMe
from product_app.views import getProfile

# Swagger settings
schema_view = get_schema_view(
   openapi.Info(
      title="Bolt API",
      default_version='v1',
      description="Bolt API. Powered by CODE TECH ACADEMY",
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/getMe/', getProfile, name='getMe'),

    # Swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # API
    path('api/v1/', include('product_app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)