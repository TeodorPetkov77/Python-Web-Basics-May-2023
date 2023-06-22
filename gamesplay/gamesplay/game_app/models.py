from django.core.validators import MinValueValidator
from django.db import models

from gamesplay.game_app.validators import validate_rating


class Game(models.Model):
    CATEGORY_CHOICES = [
        ("Action", "Action"),
        ('Adventure', "Adventure"),
        ('Puzzle', "Puzzle"),
        ('Strategy', "Strategy"),
        ('Sports', "Sports"),
        ('Board/Card Game', "Board/Card Game"),
        ('Other', "Other"),
    ]

    MAX_TITLE_LEN = 30
    MAX_CATEGORY_LEN = 15

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LEN,
        choices=CATEGORY_CHOICES,
        null=False,
        blank=False,

    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=[
            validate_rating
        ]
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1)
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )


