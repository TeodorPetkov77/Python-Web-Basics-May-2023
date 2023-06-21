from django.core import validators
from django.db import models
from car_collection.profile_app.validators import CustomMinLenValidator


class Profile(models.Model):
    MIN_USERNAME_LEN = 2
    MAX_USERNAME_LEN = 10
    MAX_NAMES_LEN = 30
    MAX_PASS_LEN = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=[
            CustomMinLenValidator(MIN_USERNAME_LEN),
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[
            validators.MinValueValidator(18)
        ],
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASS_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )
