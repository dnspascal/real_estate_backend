from django.db import models

from users.models import Users


# The model of the user
class Messages(models.Model):
    sender = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="sender id",
        related_name="sender_id",
    )
    receiver = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="receiver id",
        related_name="receiver_id",
    )
    message = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "users_messages"

    def __str__(self):
        return self.sender
