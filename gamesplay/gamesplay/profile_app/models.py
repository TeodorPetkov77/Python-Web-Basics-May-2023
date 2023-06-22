from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    MAX_NAMES_LEN = 30
    MAX_PASS_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(12)
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
