import random
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
                name="Post " + str(i),
                slug="Post-" + str(i),
                
            )
