from enum import Enum

from django.core import validators
from django.db import models

from myplant.myplant_app.validators import validate_first_letter_is_capital, validate_only_letters


class Profile(models.Model):
    MIN_USERNAME_LEN = 2
    MAX_USERNAME_LEN = 10
    MAX_NAMES_LEN = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=[
            validators.MinLengthValidator(MIN_USERNAME_LEN),
        ],
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        validators=[
            validate_first_letter_is_capital
        ],
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        validators=[
            validate_first_letter_is_capital
        ],
        null=False,
        blank=False
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class PlantTypes(ChoicesEnum):
    OUTDOOR_PLANTS = "Outdoor Plants"
    INDOOR_PLANTS = "Indoor Plants"


class Plant(models.Model):
    MAX_PLANT_TYPE_LEN = 14
    MIN_PLANT_NAME_LEN = 2
    MAX_PLANT_NAME_LEN = 20

    plant_type = models.CharField(
        max_length=MAX_PLANT_TYPE_LEN,
        choices=PlantTypes.choices(),
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=MAX_PLANT_NAME_LEN,
        validators=[
            validators.MinLengthValidator(MIN_PLANT_NAME_LEN),
            validate_only_letters,
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
