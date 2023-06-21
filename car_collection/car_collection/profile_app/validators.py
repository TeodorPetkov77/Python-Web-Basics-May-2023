from django.core.validators import MinLengthValidator
from django.utils.translation.trans_null import ngettext_lazy


class CustomMinLenValidator(MinLengthValidator):
    message = ngettext_lazy(
        "The username must be a minimum of %(limit_value)d chars.",
        "The username must be a minimum of %(limit_value)d chars.",
        "limit_value",
    )