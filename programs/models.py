from django.core.validators import MinValueValidator
from django.db import models


class ProgramChoice(models.Model):
    name = models.CharField(
        max_length=255,
    )
    age_min = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )
    age_max = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    class Meta:
        db_table = "program_choice"

    def __str__(self):
        return self.name
