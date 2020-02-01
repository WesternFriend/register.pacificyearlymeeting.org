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


class AccommodationPrice(models.Model):
    accommodation = models.ForeignKey(
        to="accommodations.Accommodation",
        on_delete=models.PROTECT,
        related_name="accommodation_prices"
    )
    daily_price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )

    class Meta:
        db_table = "accommodation_price"

    def __str__(self):
        return f"{ self.accommodation }"
