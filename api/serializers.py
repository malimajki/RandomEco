from rest_framework import serializers

from shop.models import Product, Category as Category_shop
from blog.models import Post, Category as Category_blog

class CategoryShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_shop
        fields = [
            "id",
            "name",
            "slug",
        ]

class CategoryBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_blog
        fields = [
            "id",
            "name",
            "slug",
        ]

class ProductSerializer(serializers.ModelSerializer):
    category = CategoryShopSerializer()
    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "name",
            "description",
            "price",
        ]

class PostSerializer(serializers.ModelSerializer):
    category = CategoryBlogSerializer()
    class Meta:
        model = Post
        fields = [
            "id",
            "category",
            "image",
            "title",
            "body",
            "created",
        ]