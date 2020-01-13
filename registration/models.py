from django.core.validators import MinValueValidator
from django.db import models


class Registrant(models.Model):
    first_name = models.CharField(
        max_length=255
    )
    last_name = models.CharField(
        max_length=255
    )
    registration_cost = models.FloatField(
        validators=[
            MinValueValidator(0)
        ]
    )

    def full_name(self):
        return f"{ self.first_name } { self.last_name }"

    def __str__(self):
        return self.full_name()
