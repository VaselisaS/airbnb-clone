import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations.models import Reservation
from rooms.models import Room
from users.models import User


NAME = "reservations"


class Command(BaseCommand):
    help = f"This command create {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help=f"How many {NAME} you want to create",
            type=int,
        )

    def handle(self, *args, **options):
        number = options.get("number")
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Reservation,
            number,
            {
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(2, 10)),
                "check_in": lambda x: datetime.now(),
                "room": lambda x: random.choice(rooms),
                "guest": lambda x: random.choice(users),
            },
        )

        seeder.execute()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {number} {NAME}")
        )
