from django.core.exceptions import ValidationError

from petstagram.utils.convert_b_to_mb import convert_mb_to_b

MAX_IMAGE_MB_LIMIT = 5


def validate_file_size(image_object):
    limit_in_bytes = convert_mb_to_b(MAX_IMAGE_MB_LIMIT)
    if image_object.size > limit_in_bytes:
        raise ValidationError(f"The maximum file size that can be uploaded is {MAX_IMAGE_MB_LIMIT}MB.")
