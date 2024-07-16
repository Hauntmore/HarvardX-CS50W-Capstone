"""
The Uniform Resource Locator (URL) configuration for the Capstone project. This file defines routes that map specific URLs to their corresponding views. For more information on this file please see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("authentication/", include("apps.authentication.urls")),
    path("event/", include("apps.event.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
