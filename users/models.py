from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django_resized import ResizedImageField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image =ResizedImageField(size=[600,600], quality=85, upload_to='avatars/', null=True, blank=True) 
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=40, null=True, blank=True)
    zip = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('img/avatar_default.png')
        return avatar
    