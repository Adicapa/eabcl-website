from typing import Text
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='products/', blank=True)
    

class Products(models.Model):
    name = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40)
    name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    image = models.ImageField(upload_to='menu/', blank=True)
    upload = models.FileField(upload_to='menu/')
    upload = models.FileField(upload_to='menu/')
    image = models.ImageField(upload_to='menu/', blank=True)
    price = models.FloatField()
    
    
    
    def __self__(self):
        return self.name
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/', blank=True)
    
    

