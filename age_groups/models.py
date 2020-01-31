from django.db import models


class AgeGroup(models.Model):
    name = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = "age_group"

    def __str__(self):
        return self.name
