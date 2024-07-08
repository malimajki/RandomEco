from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Generates User for testing"

    def handle(self, *args, **options):

        for i in range(8):
            User.objects.create(
                username=f"user{i+100}",
                email=f"user{i+100}@gmail.com",
                password="password",               
            )
