from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from django.conf import settings

class Command(BaseCommand):
    help = 'Add social applications for Django Allauth'

    def handle(self, *args, **kwargs):
        GOOGLE_CLIENT_ID = '14148621159-gd6da9pu9q3dgp9qs3v5mqrqig15q0ab.apps.googleusercontent.com'
        GOOGLE_CLIENT_SECRET = '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'

        # Google
        google_app, created = SocialApp.objects.get_or_create(
            provider='google',
            name='Google',
            client_id=GOOGLE_CLIENT_ID,
            secret=GOOGLE_CLIENT_SECRET
        )
        if created:
            google_app.sites.add(settings.SITE_ID)
            self.stdout.write(self.style.SUCCESS('Successfully created Google social application'))
        else:
            self.stdout.write(self.style.WARNING('Google social application already exists'))