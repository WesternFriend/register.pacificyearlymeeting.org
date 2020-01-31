from django.db import models


class Accommodation(models.Model):
    name = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = "accommodation"

    def __str__(self):
        return self.name


class AccommodationPrice(models.Model):
    accommodation = models.ForeignKey(
        to="accommodations.Accommodation",
        on_delete=models.PROTECT,
        related_name="accommodation_prices"
    )
    age_group = models.ForeignKey(
        to="age_groups.AgeGroup",
        on_delete=models.PROTECT,
        related_name="accommodation_prices"
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )

    class Meta:
        db_table = "accommodation_price"
        unique_together = ("accommodation", "age_group")

    def __str__(self):
        return f"{ self.accommodation } for age group { self.age_group }"
