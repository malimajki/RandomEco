import random
from django.shortcuts import render
from shop.models import Product
from blog.models import Post

def home(request):
    products = list(Product.objects.all())
    random.shuffle(products)
    products = products

    posts = Post.objects.all()[:4]

    context = {
        "products":products,
        "posts":posts,
        }

    return render (request, "home/home.html", context)