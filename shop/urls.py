from django.urls import path

from.views import shop, product, add_to_cart, update_cart, checkout

app_name = 'shop'

urlpatterns = [
    path('', shop, name='home'),
    path('product/<slug:slug>', product, name='product' ),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', update_cart, name='update_cart'),
    path('checkout/', checkout, name='checkout'),
]
