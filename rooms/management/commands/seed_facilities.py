from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command create facilities"

    def handle(self, *args, **options):
        facilities = [
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
        ]
        for facility in facilities:
            Facility.objects.create(name=facility)
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created facilities length {len(facilities)}"
            )
        )
