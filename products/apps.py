from django.apps import AppConfig



# To register this category model in our admin

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
