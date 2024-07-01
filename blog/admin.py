from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)
@admin.register(Category)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}