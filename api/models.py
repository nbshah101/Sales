from __future__ import unicode_literals
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

from django.db import models


class Sales(models.Model):
    vin = models.CharField(max_length=20, blank=False)
    make = models.CharField(max_length=255, blank=False)
    model = models.CharField(max_length=255, blank=False)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)],
        help_text="Use the following format: <YYYY>")
    price = models.CharField(max_length=255, blank=False)
    buyer = models.CharField(max_length=255, blank=False)
    seller = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}-{}".format(self.vin, self.model)
