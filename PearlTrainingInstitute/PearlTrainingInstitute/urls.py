from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include("django_admin_kubi.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/school/', include('school.urls')),
    path('api/staff/', include('staff.urls')),
    path('api/admissions/', include('admissions.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
