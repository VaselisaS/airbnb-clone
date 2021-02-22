from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):
    help = "This command create room types"

    def handle(self, *args, **options):
        room_types = [
            "Entire place",
            "Private room",
            "Hotel room",
            "Shared room",
        ]
        for room_type in room_types:
            RoomType.objects.create(name=room_type)
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created room types length {len(room_types)}"
            )
        )
