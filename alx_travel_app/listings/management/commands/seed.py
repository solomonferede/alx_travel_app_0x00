from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            default=10,
            help='Number of listings to create'
        )

    def handle(self, *args, **options):
        fake = Faker()
        number = options['number']

        # Get all users (we need at least one user)
        users = User.objects.all()
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create some users first.'))
            return

        listings_created = 0
        for _ in range(number):
            owner = random.choice(users)
            title = fake.sentence(nb_words=4)
            description = fake.paragraph(nb_sentences=3)
            price_per_night = round(random.uniform(50, 500), 2)
            location = fake.city()

            Listing.objects.create(
                owner=owner,
                title=title,
                description=description,
                price_per_night=price_per_night,
                location=location
            )
            listings_created += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully created {listings_created} listings.'))
