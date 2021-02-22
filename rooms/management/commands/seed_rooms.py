import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms.models import Room, RoomType, Photo, Amenity, Facility, Rule
from users.models import User


class Command(BaseCommand):
    help = "This command create rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help="How many rooms you want to create",
            type=int,
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = User.objects.all()
        room_types = RoomType.objects.all()
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        rules = Rule.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(5, 150),
                "guests": lambda x: random.randint(1, 5),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )

        room_ids = flatten(list(seeder.execute().values()))

        for room_id in room_ids:
            room = Room.objects.get(pk=room_id)
            magic_number = random.randint(1, 10)
            for _ in range(3, random.randint(5, 10)):
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for amenity in amenities:
                if magic_number % 2 == 0:
                    room.amenities.add(amenity)
            for facility in facilities:
                if magic_number % 2 == 0:
                    room.facilities.add(facility)
            for rule in rules:
                if magic_number % 2 == 0:
                    room.house_rules.add(rule)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {number} rooms")
        )
