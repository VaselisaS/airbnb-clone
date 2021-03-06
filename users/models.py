import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import strip_tags
from django.template.loader import render_to_string


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
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self, domain):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html",
                {"secret": secret, "domain": domain},
            )
            send_mail(
                "Verify AirBnb account",
                strip_tags(html_message),
                settings.EMAIL_HOST_USER,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
