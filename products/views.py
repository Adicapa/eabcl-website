from django.shortcuts import render
from products.models import Products, ProductImage


def home(request):
    # retrive all products from database
    products = Products.objects.all()
    product_images = ProductImage.objects.all()
    # filter the only 5 categories we need
    insecticides = []
    fertilizers = []
    herbicides = []
    fungicides= []
    for product in products:
        if product.category.name == 'Insecticides':
            insecticides.append(product)

        if product.category.name == 'Fertilizers':
            fertilizers.append(product)

        if product.category.name == 'Herbicides':
            herbicides.append(product)

        if product.category.name == 'Fungicides':
            fungicides.append(product)

    
    # compose and return the data
    return_payload = {
        'fertizers': fertilizers,
        'fungicides': fungicides,
        'herbicides': herbicides,
        'insecticides': insecticides,
        'product_images': product_images,
        
    }
    return render(request, 'index.html', return_payload)
