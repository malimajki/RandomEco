from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from.models import Category, Post, Comment, LikedComment, Reply, LikedPost, LikedReply
from.forms import CommentCreateForm, ReplyCreateForm

def home_view(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(created__lt=timezone.now())

    active_category = request.GET.get('category', '')

    if active_category:
        posts = posts.filter(category__slug=active_category)

    query = request.GET.get('blog_search', '')

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(body__icontains=query))
        
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "categories":categories,
        "posts":posts,
        'active_category':active_category,
        "page_obj": page_obj,
    }

    return render (request, "blog/home.html", context)

def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    commentform = CommentCreateForm()
    replyform = ReplyCreateForm()
    
    if request.htmx:
        if 'top' in request.GET:
            comments = post.comments.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by('-num_likes')
        else:
            comments = post.comments.all()
        return render(request, 'snippets/loop_postpage_comments.html', {'comments': comments, 'replyform': replyform})
    
    
    context = {
        'post' : post,
        'commentform' : commentform,
        'replyform' : replyform,
    }
    
    return render(request, 'blog/post_page.html', context)

@login_required 
def comment_sent(request, pk):
    post = get_object_or_404(Post, id=pk)
    commentform = CommentCreateForm()
    
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post            
            comment.save()
            
    context = {
        'post' : post,
        'comment': comment,
        'commentform': commentform
    }

    return render(request, 'snippets/add_comment.html', context)


@login_required 
def reply_sent(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    replyform = ReplyCreateForm()
    
    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment            
            reply.save()
            
    context = {
        'reply' : reply,
        'comment': comment,
        'replyform': replyform
    }

    return render(request, 'snippets/add_reply.html', context)


@login_required
def comment_delete_view(request, pk):
    post = get_object_or_404(Comment, id=pk, author=request.user)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Comment deleted')
        return redirect('post', post.parent_post.id )
        
    return render(request, 'a_blog/comment_delete.html', {'comment' : post})


@login_required
def reply_delete_view(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)
    
    if request.method == "POST":
        reply.delete()
        messages.success(request, 'Reply deleted')
        return redirect('post', reply.parent_comment.parent_post.id )
        
    return render(request, 'a_blog/reply_delete.html', {'reply' : reply})


def like_toggle(model):
    def inner_func(func):
        def wrapper(request, *args, **kwargs):
            post = get_object_or_404(model, id=kwargs.get('pk'))
            user_exist = post.likes.filter(username=request.user.username).exists()
            
            if user_exist:
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
                
            return func(request, post)
        return wrapper
    return inner_func


@login_required
@like_toggle(Post)
def like_post(request, post):   
    return render(request, 'snippets/likes.html', {'post' : post })


@login_required
@like_toggle(Comment)
def like_comment(request, post):   
    return render(request, 'snippets/likes_comment.html', {'comment' : post })


@login_required
@like_toggle(Reply)
def like_reply(request, post):   
    return render(request, 'snippets/likes_reply.html', {'reply' : post })

