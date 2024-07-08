from django import forms
from blog.models import Post
from django.forms.widgets import DateTimeInput
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'body', 'category', 'public', 'created']
        widgets = {
            'body': SummernoteWidget(),
            'created': DateTimeInput(attrs={'type': 'datetime-local'}),
        }