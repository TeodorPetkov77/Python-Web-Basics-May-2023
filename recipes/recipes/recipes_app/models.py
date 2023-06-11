from django.db import models


class Recipe(models.Model):
    MAX_TITLE_LEN = 30
    MAX_INGREDIENTS_LEN = 250

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
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

    ingredients = models.CharField(
        max_length=MAX_INGREDIENTS_LEN,
        null=False,
        blank=False,
    )

    time = models.IntegerField(
        null=False,
        blank=False,
    )