from django.core.validators import MinValueValidator
from django.db import models

from registration.models import Registrant


class Payment(models.Model):
    amount = models.FloatField()


class RegistrantPayment(models.Model):
    registrant = models.ForeignKey(
        to=Registrant,
        related_name="payments",
        on_delete=models.PROTECT,
    )
    payment = models.ForeignKey(
        to=Payment,
        related_name="registrants",
        on_delete=models.PROTECT,
    )
    amount = models.FloatField(
        validators=[
            MinValueValidator(0)
        ]
    )
