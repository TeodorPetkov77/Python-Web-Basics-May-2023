from django.core import exceptions


def validate_first_letter_is_capital(value):
    if not value[0].isupper():
        raise exceptions.ValidationError("Your name must start with a capital letter!")


def validate_only_letters(value):
    for letter in value:
        if not letter.isalpha() and letter != " ":
            raise exceptions.ValidationError("Plant name should contain only letters!")