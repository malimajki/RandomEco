from django.urls import path
from api.views import ProductList, PostList

app_name="api"

urlpatterns = [
    path('products', ProductList.as_view(), name="product-view"),
    path('posts', PostList.as_view(), name="post-view"),
]