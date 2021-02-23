import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms.models import Room, RoomType, Photo, Amenity, Facility, Rule
from users.models import User

NAME = "rooms"


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
        count_models = options.get("number")
        users = User.objects.all()
        room_types = RoomType.objects.all()
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        rules = Rule.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Room,
            count_models,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(users),
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
            for _ in range(3, random.randint(5, 10)):
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            self.add_attributes(room, amenities, "amenity")
            self.add_attributes(room, facilities, "facility")
            self.add_attributes(room, rules, "rule")

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {count_models} {NAME}")
        )

    def add_attributes(self, obj, attributes, name_attr):
        start_slice = random.randint(0, int(len(attributes) / 2))
        end_slice = random.randint(int(len(attributes) / 2), len(attributes))
        to_add = attributes[start_slice:end_slice]
        list_adding_attr = {
            "amenity": lambda: obj.amenities.add(*to_add),
            "facility": lambda: obj.facilities.add(*to_add),
            "rule": lambda: obj.house_rules.add(*to_add),
        }
        list_adding_attr[name_attr]()
