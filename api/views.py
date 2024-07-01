from rest_framework import generics
from shop.models import Product, Category as Category_shop
from blog.models import Post, Category as Category_blog
from .serializers import ProductSerializer, PostSerializer, CategoryBlogSerializer, CategoryShopSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryBlogList(generics.ListAPIView):
    queryset = Category_blog.objects.all()
    serializer_class = CategoryBlogSerializer

class CategoryShopList(generics.ListAPIView):
    queryset = Category_shop.objects.all()
    serializer_class = CategoryShopSerializer