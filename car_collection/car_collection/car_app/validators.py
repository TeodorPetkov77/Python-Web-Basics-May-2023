from django.core import exceptions

MAX_YEAR = 2049
MIN_YEAR = 1980


def validate_year(value):
    if not MIN_YEAR <= value <= MAX_YEAR:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")
