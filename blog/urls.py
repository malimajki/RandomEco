from django.urls import path
from.views import home_view, post_page_view, like_comment, like_post, like_reply, comment_sent, comment_delete_view, reply_sent, reply_delete_view

app_name = "blog"

urlpatterns = [
    path('', home_view, name='home'),
    path('category/<slug:slug>/', home_view, name="category"), 
    path('post/<pk>/', post_page_view, name="post"),

    path('like/post/<pk>/', like_post, name="like-post"), 
    path('like/comment/<pk>/', like_comment, name="like-comment"), 
    path('like/reply/<pk>/', like_reply, name="like-reply"),

    path('commentsent/<pk>/', comment_sent, name='comment-sent'), 
    path('comment/delete/<pk>/', comment_delete_view, name='comment-delete'),
    path('replysent/<pk>/', reply_sent, name='reply-sent'), 
    path('reply/delete/<pk>/', reply_delete_view, name='reply-delete'),
]
