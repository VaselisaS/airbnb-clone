import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users.models import User
from rooms.models import Room


class Command(BaseCommand):
    help = "This command create reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            help="How many reviews you want to create",
            type=int,
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(
            Review,
            number,
            {
                "cleanliness": lambda x: random.randint(0, 5),
                "accuracy": lambda x: random.randint(0, 5),
                "communication": lambda x: random.randint(0, 5),
                "location": lambda x: random.randint(0, 5),
                "check_in": lambda x: random.randint(0, 5),
                "value": lambda x: random.randint(0, 5),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {number} reviews")
        )
