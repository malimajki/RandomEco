from django.contrib import admin
from . models import Product, Category, Order, OrderItem, ProductImage, Cart

class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "quantity", "subtotal")



class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine]
    prepopulated_fields = {"slug":("name",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInLine]
    list_display = ('id', 'user', 'email', 'created_at')
    search_fields = ('user__username', 'email', 'id')



admin.site.register(Product, ProductAdmin),
admin.site.register(Category, CategoryAdmin),
admin.site.register(Order, OrderAdmin),
admin.site.register(OrderItem),