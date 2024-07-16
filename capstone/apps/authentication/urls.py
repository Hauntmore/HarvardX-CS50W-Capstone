"""
URL configuration for the Authentication application.

This module defines URL patterns for handling authentication-related views,
such as 'authentication/login', 'authentication/logout', password, and account management, etc.

Each URL pattern maps a specific URL path to its corresponding view function.

For more information on Django URL routing, see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
