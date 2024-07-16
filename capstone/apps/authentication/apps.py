"""
The application configuration module for the Authentication application.

This module defines a class used to customize application-level settings and initialization behavior.

For more information on Django application configuration, go see:
https://docs.djangoproject.com/en/5.0/ref/applications/#configuring-applications
"""

from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Configuration class for the authentication application.

    This class defines configuration settings and initialization behavior specific to the Authentication app, allowing customization of attributes such as the default name and initialization methods.

    Attributes:
        name (str): The name of the Django application, typically 'authentication'.

        verbose_name (str): A human-readable name for the application displayed in the Django administration panel.
    """

    name = "apps.authentication"

    verbose_name = "Authentication"
