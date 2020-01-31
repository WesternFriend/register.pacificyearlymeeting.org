from django.db import models


class EventDay(models.Model):
    date = models.DateField(
        help_text="Choose one of the event days",
        unique=True
    )
    partial_day_discount = models.IntegerField(
        null=True,
        blank=True,
        help_text="Enter the optional amount in USD that each day registration should be discounted on this date."
    )

    class Meta:
        db_table = "event_day"
