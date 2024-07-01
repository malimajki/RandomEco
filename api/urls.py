from django.urls import path
from api.views import ProductList, PostList, CategoryBlogList, CategoryShopList

app_name="api"

urlpatterns = [
    path('products', ProductList.as_view(), name="product-view"),
    path('category_products', CategoryShopList.as_view(), name="category-product-view"),
    path('posts', PostList.as_view(), name="post-view"),
    path('category_posts', CategoryBlogList.as_view(), name="category-posts-view"),
]