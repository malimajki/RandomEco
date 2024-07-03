from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from allauth.account.utils import send_email_confirmation
from .forms import ProfileForm, SignUpForm
from django.contrib.auth.views import LoginView
from shop.models import Order

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})



def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
        user = request.user
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
        
    if request.htmx:   
        if 'top-comments' in request.GET:
            comments = profile.user.comments.annotate(num_likes=Count('likes'))
            return render(request, 'snippets/loop_profile_comments.html', { 'comments': comments,})
        elif 'liked-posts' in request.GET:
            posts = profile.user.likedposts.order_by('-likedpost__created') 
            return render(request, 'snippets/loop_profile_posts.html', { 'posts': posts })
        elif 'my-orders' in request.GET:
            orders = Order.objects.filter(user=user) 
            return render(request, 'snippets/loop_profile_orders.html', { 'orders': orders })
        
    context = {
        'profile' : profile, 
    }
    
    return render(request, 'users/profile.html', context)

@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
 
    template = 'users/profile_edit.html'
         
    return render(request, template, {'form':form})

@login_required
def profile_delete_view(request):
    user = request.user
    
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('home')
    
    return render(request, 'users/profile_delete.html' )


def profile_verify_email (request):
    send_email_confirmation(request, request.user)
    return(redirect('profile'))