import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from rooms.models import Room
from users.models import User


class Command(BaseCommand):
    help = "This command create lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help="How many lists you want to create",
            type=int,
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = User.objects.all()
        rooms = Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            List,
            number,
            {
                "user": lambda x: random.choice(all_users),
            },
        )

        list_ids = flatten(list(seeder.execute().values()))
        for pk in list_ids:
            list_model = List.objects.get(pk=pk)
            start_slice = random.randint(0, len(rooms) / 2)
            end_slice = random.randint(len(rooms) / 2, len(rooms))
            to_add = rooms[start_slice:end_slice]
            list_model.rooms.add(*to_add)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {number} lists")
        )
