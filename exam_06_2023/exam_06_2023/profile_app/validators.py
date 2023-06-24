from django.core import exceptions


def validate_first_letter(value):
    if not value[0].isalpha():
        raise exceptions.ValidationError("Your name must start with a letter!")
