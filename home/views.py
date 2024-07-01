import random
from django.shortcuts import render
from shop.models import Product

def home(request):
    products = list(Product.objects.all())
    random.shuffle(products)
    products = products

    context = {
        "products":products,
    }

    return render (request, "base.html", context)