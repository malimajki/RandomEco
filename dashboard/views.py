from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from shop.models import Product, Order
from django.contrib.auth.models import User
from .forms import PostForm

def index(request):
    products = Product.objects.all()
    posts = Post.objects.all()
    users = User.objects.all()
    orders = Order.objects.all()
    

    context = {
        "products":products,
        "posts":posts,
        "users":users,
        "orders":orders,
        }

    return render (request, "dashboard/index.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'dashboard/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'dashboard/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/post_form.html'
    success_url = reverse_lazy('dashboard:post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/post_form.html'
    success_url = reverse_lazy('dashboard:post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'dashboard/post_confirm_delete.html'
    success_url = reverse_lazy('dashboard:post_list')