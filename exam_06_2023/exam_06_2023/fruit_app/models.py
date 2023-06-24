from django.core.validators import MinLengthValidator
from django.db import models

from exam_06_2023.fruit_app.validators import validate_all_letters


class Fruit(models.Model):
    MAX_FRUIT_NAME_LEN = 30
    MIN_FRUIT_NAME_LEN = 2

    name = models.CharField(
        max_length=MAX_FRUIT_NAME_LEN,
        validators=[
            MinLengthValidator(MIN_FRUIT_NAME_LEN),
            validate_all_letters,
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

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

