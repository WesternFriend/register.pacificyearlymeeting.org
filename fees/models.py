from django.db import models
from django.core.validators import MinValueValidator


class DayAttenderFee(models.Model):
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
    daily_fee = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    class Meta:
        db_table = "day_attender_fee"

    def __str__(self):
        return f"Age: {self.age_min} to {self.age_max}. Daily fee: {self.daily_fee}"


class AccommodationFee(models.Model):
    age_min = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    age_max = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    accommodation = models.ForeignKey(
        to="accommodations.Accommodation",
        on_delete=models.PROTECT,
        related_name="accommodation_prices"
    )
    daily_fee = models.DecimalField(
        default=True,
        decimal_places=2,
        max_digits=10
    )
    full_week_fee = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
    )

    class Meta:
        db_table = "accommodation_fee"

    def __str__(self):
        return f"{ self.accommodation }"
