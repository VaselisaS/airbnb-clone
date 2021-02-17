from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """ Absract Item """

    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class RoomType(AbstractItem):
    """ Room Type Model Definition """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Fasility(AbstractItem):
    """ Fasility Model Definition """

    class Meta:
        verbose_name_plural = "Fasilities"


class HouseRule(AbstractItem):
    """ House Rule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Rule(AbstractItem):
    """ Rule Model Definition """


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        "RoomType",
        on_delete=models.SET_NULL,
        null=True
    )
    amenities = models.ManyToManyField("Amenity", blank=True)
    fasilities = models.ManyToManyField("Fasility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
