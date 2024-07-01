import random
from datetime import datetime
from django.core.management.base import BaseCommand
from blog.models import User, Post, Category


class Command(BaseCommand):
    help = "Generates Products for testing"

    def handle(self, *args, **options):

        categories = [
            "Java",
            "Python",
            "C++",
            "GO",
            "PHP"
        ]

        for category in categories:
            Category.objects.get_or_create(name=category, slug=category)
            
        
        categories = Category.objects.all()
        for i in range(20):
            Post.objects.create(
                category=random.choice(categories),
                title="Post " + str(i),
                image = "img/image_not_found.png",
                body = "VS Code has great support for source code formatting. The editor has two explicit format actions: Format Document (Ctrl+Shift+I) - Format the entire active file. Format Selection (Ctrl+K Ctrl+F) - Format the selected text.",
                created=datetime.now(),
                
            )
