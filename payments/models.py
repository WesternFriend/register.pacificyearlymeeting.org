from django.core.validators import MinValueValidator
from django.db import models

from registration.models import Registrant

PAYMENT_SOURCE_CHOICES = [
    ("online", "Online"),
    ("check", "Check"),
    ("cash", "Cash"),
]


class Payment(models.Model):
    amount = models.FloatField()

    source = models.CharField(
        max_length=255,
        choices=PAYMENT_SOURCE_CHOICES,
    )

    paid_by = models.CharField(
        max_length=255,
        help_text="Name of person, meeting, or organization that made this payment."
    )

    def __str__(self):
        return f"ID #{self.id} - { self.amount } ({ self.source }) paid by { self.paid_by }"


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
