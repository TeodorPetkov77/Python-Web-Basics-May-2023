from django.core.validators import MinLengthValidator
from django.db import models

from exam_06_2023.profile_app.validators import validate_first_letter


class Profile(models.Model):
    MAX_FIRST_NAME_LEN = 25
    MIN_FIRST_NAME_LEN = 2
    MAX_LAST_NAME_LEN = 35
    MIN_LAST_NAME_LEN = 1
    MAX_EMAIL_LEN = 40
    MAX_PASS_LEN = 20
    MIN_PASS_LEN = 8

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        validators=[
            MinLengthValidator(MIN_FIRST_NAME_LEN),
            validate_first_letter,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        validators=[
            MinLengthValidator(MIN_LAST_NAME_LEN),
            validate_first_letter,
        ],
        null=False,
        blank=False
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=MAX_EMAIL_LEN,
    )

    password = models.CharField(
        max_length=MAX_PASS_LEN,
        validators=[
            MinLengthValidator(MIN_PASS_LEN)
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    age = models.IntegerField(
        default=18,
        null=True,
        blank=True,
    )
