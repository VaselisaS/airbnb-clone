from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """ Conversation Model Definition """

    partisipants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.partisipants.all():
            usernames.append(user.username)
        return f"{self.created.strftime('%d-%m-%Y %H:%M')}: {', '.join(usernames)}"

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of messages"

    def count_partisipants(self):
        return self.partisipants.count()

    count_partisipants.short_description = "Number of partisipants"


class Message(core_models.TimeStampedModel):
    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
