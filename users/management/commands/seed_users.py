from django.core.management.base import BaseCommand
from users.models import User
from django_seed import Seed


class Command(BaseCommand):
    help = "This command create users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help="How many users you want to create",
            type=int,
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {number} users")
        )
