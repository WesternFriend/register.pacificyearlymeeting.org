from django.core.validators import MinValueValidator
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from registration.models import Registrant

PAYMENT_SOURCE_CHOICES = [
    ("online", "Online"),
    ("check", "Check"),
    ("cash", "Cash"),
]


class Payment(ClusterableModel):
    """
    Represents a payment made,
    E.g. a check that was paid
    """
    amount = models.DecimalField(
        help_text="Amount for this payment, in USD ($)",
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ]
    )

    source = models.CharField(
        max_length=255,
        choices=PAYMENT_SOURCE_CHOICES,
        help_text="Method by which this payment was made"
    )

    paid_by = models.CharField(
        max_length=255,
        help_text="Name of person, meeting, or organization that made this payment"
    )

    panels = [
        FieldPanel("paid_by"),
        FieldPanel("source"),
        FieldPanel("amount"),
        InlinePanel("allocations", heading="Allocated to registrants"),
    ]

    def __str__(self):
        return f"ID #{self.id} - { self.amount } ({ self.source }) paid by { self.paid_by }"


class Allocation(models.Model):
    """
    Represents a portion of a payment that is applied to a registrant balance due
    """
    registrant = models.ForeignKey(
        to=Registrant,
        related_name="payment_allocations",
        on_delete=models.PROTECT,
    )
    payment = ParentalKey(
        to=Payment,
        related_name="allocations",
        on_delete=models.PROTECT,
        help_text="Choose a registrant to which this payment should be applied"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ]
    )
