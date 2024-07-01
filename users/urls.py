from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.views import *

app_name = "profile"

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    path('profile/', profile_view, name="profile"),
    path('profile/edit/', profile_edit_view, name="profile-edit"), 
    path('profile/verifyEmial/', profile_verify_email, name="profile-verify-email"), 
    path('profile/delete/', profile_delete_view, name="profile-delete"),
    path('profile/onboarding/', profile_edit_view, name="profile_onboarding"),
    path('profile/<username>/', profile_view, name="userprofile"),
]