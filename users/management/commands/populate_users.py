import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Generates Products for testing"

    def handle(self, *args, **options):

        for i in range(8):
            User.objects.create(
                username=f"user{i}",
                email=f"user{i}@gmail.com",
                password="password123"
            )
