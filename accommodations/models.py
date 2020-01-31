from django.db import models


class Accommodation(models.Model):
    name = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = "accommodation"
