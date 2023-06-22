from django.core import exceptions

MIN_RATING = 0.1
MAX_RATING = 5.0


def validate_rating(value):
    if not MIN_RATING <= value <= MAX_RATING:
        raise exceptions.ValidationError(f"Rating must be between "
                                         f"{MIN_RATING} and {MAX_RATING}")