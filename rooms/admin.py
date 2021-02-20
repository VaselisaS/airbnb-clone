from django.contrib import admin
from . import models


@admin.register(
    models.RoomType,
    models.Amenity,
    models.Facility,
    models.HouseRule,
    models.Rule,
)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "host",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    ordering = ("name",)

    filter_horizontal = ("amenities", "facilities", "house_rules")

    search_fields = ("=city", "^host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
