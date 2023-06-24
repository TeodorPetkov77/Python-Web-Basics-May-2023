from django.core import exceptions


def validate_all_letters(value):
    for letter in value:
        if not letter.isalpha() and letter != " ":
            raise exceptions.ValidationError('Fruit name should contain only letters!')