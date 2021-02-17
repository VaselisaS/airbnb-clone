from django.contrib import admin
from . import models


@admin.register(
    models.RoomType,
    models.Amenity,
    models.Fasility,
    models.HouseRule,
    models.Rule
)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
