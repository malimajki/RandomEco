from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include('api.urls' ,namespace='api')),
    path('accounts/', include('allauth.urls')),
    path('', home, name="home"),
    path("shop/", include('shop.urls' ,namespace='shop')),
    path("blog/", include('blog.urls' ,namespace='blog')),
    path("profile/", include('users.urls' ,namespace='profile')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)