"""
Configure Cart application
"""
from django.apps import AppConfig


class CartConfig(AppConfig):
    """
    Cart App Configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
