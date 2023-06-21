from enum import Enum

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection.car_app.validators import validate_year


class Car(models.Model):
    MODEL_CHOICES = [
        ("Sports Car", "Sports Car"),
        ('Pickup', "Pickup"),
        ('Crossover', "Crossover"),
        ('Minibus', "Minibus"),
        ('Other', "Other"),
    ]

    MAX_CAR_TYPE_LEN = 10
    MIN_MODEL_LEN = 2
    MAX_MODEL_LEN = 20

    type = models.CharField(
        max_length=MAX_CAR_TYPE_LEN,
        choices=MODEL_CHOICES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LEN,
        validators=[
            MinLengthValidator(MIN_MODEL_LEN)
        ],
        null=False,
        blank=False,

    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validate_year
        ]
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1)
        ]
    )
