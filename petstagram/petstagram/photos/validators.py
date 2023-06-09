from petstagram.utils.convert_mb_to_b import convert_mb_to_b

MAX_SIZE_MB = 5


def validate_file_size(image_object):
    if image_object.size > convert_mb_to_b(MAX_SIZE_MB):
        raise ValueError(f"The maximum file size that can be uploaded is {MAX_SIZE_MB} MB")