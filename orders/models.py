from django.db import models

from property.models import Properties
from users.models import Users

#  Model of the order of a user


class Order(models.Model):
    property = models.ForeignKey(
        Properties, on_delete=models.CASCADE, verbose_name="property id"
    )
    property_owner = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="user id",
        related_name="property_owner",
    )

    client = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="client_order",
        verbose_name="user id",
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField()


    class Meta:
        db_table="orders"

        
    def __str__(self):
        return self.property_owner
