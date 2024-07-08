from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "dashboard"

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<str:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<str:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]