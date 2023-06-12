from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    MAX_NAMES_LEN = 20

    first_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        max_length=MAX_NAMES_LEN,
        null=False,
        blank=False
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1)
        ]
    )
    image_url = models.URLField(
        null=True,
        blank=True
    )


class Note(models.Model):
    MAX_TITLE_LEN = 30
    MAX_CONTENT_LEN = 100

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
        null=False,
        blank=False
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    content = models.TextField(
        null=False,
        blank=False,
        max_length=MAX_CONTENT_LEN,
    )
