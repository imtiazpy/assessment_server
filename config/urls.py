from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


admin.site.site_header = 'Assessment'
admin.site.site_title = 'Assessment Admin Panel'
admin.site.index_title = 'Assessment Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
        path('users/', include('users.api.urls', namespace='users')),
    ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

API_INFO = openapi.Info(
    title = 'Assessment API',
    default_version = 'v1',
    description = 'API documentation of Assessment App'
)

API_DOCS_SCHEMA_VIEWS = get_schema_view(
    API_INFO,
    public = True,
    permission_classes = [IsAuthenticated, ],
)

urlpatterns += [
    path('api-docs/', API_DOCS_SCHEMA_VIEWS.with_ui("swagger", cache_timeout=0), name='API Playground')
]
