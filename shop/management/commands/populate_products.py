import random
from django.core.management.base import BaseCommand
from shop.models import User, Product, Category


class Command(BaseCommand):
    help = "Generates Products for testing"

    def handle(self, *args, **options):

        categories = [
            "Bills",
            "Food",
            "Clothes",
            "Medical",
            "Housing"
        ]

        for category in categories:
            Category.objects.get_or_create(name=category, slug=category)
        
        categories = Category.objects.all()
        for i in range(8):
            Product.objects.create(
                category=random.choice(categories),
                name="product " + str(i),
                slug="product-" + str(i),
                price=random.uniform(200, 500),
                description="description"
            )
