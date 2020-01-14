from django.core.validators import MinValueValidator
from django.db import models


class Registrant(models.Model):
    """
    Represents a person who will attend the annual session.
    """
    first_name = models.CharField(
        max_length=255
    )
    last_name = models.CharField(
        max_length=255
    )
    needs_ada_accessible_accommodations = models.BooleanField()

    registration_cost = models.FloatField(
        validators=[
            MinValueValidator(0)
        ]
    )

    def full_name(self):
        return f"{ self.first_name } { self.last_name } (${ self.registration_cost })"

    def __str__(self):
        return self.full_name()
