from rest_framework import generics
from shop.models import Product
from blog.models import Post
from .serializers import ProductSerializer, PostSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer