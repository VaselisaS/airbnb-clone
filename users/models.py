from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    ]

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_UKRAIN = "ua"

    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_UKRAIN, "Ukrain"),
    ]

    CURRENCY_USD = "usd"
    CURRENCY_UAH = "uah"

    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_UAH, "UAH"),
    ]

    bio = models.TextField(blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True
    )
    avatar = models.ImageField(blank=True, upload_to="avatars")
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=3,
        blank=True,
        default=LANGUAGE_ENGLISH,
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=3,
        blank=True,
        default=CURRENCY_USD,
    )
    superhost = models.BooleanField(default=False)
