from django.apps import AppConfig
from django.contrib import admin
from .models import Products


# To register this category model in our admin
admin.site.register(Products)

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Products'
