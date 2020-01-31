from django.db import models


class DietaryNeed(models.Model):
    name = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = "dietary_need"

    def __str__(self):
        return self.name


class MealOption(models.Model):
    name = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = "meal_option"

    def __str__(self):
        return self.name
