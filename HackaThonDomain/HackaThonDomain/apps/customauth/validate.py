from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.functional import SimpleLazyObject
import re

def _lazy_re_compile(regex, flags=0):
    """Lazily compile a regex with flags."""
    def _compile():
        # Compile the regex if it was not passed pre-compiled.
        if isinstance(regex, (str, bytes)):
            return re.compile(regex, flags)
        else:
            assert not flags, (
                'flags must be empty if regex is passed pre-compiled'
            )
            return regex
    return SimpleLazyObject(_compile)

@deconstructible
class CustomEmailValidator(validators.EmailValidator):
    message = ('Введите корректный e-mail')
    user_regex = _lazy_re_compile(
        r'^\w+', re.IGNORECASE
    )
    domain_regex = _lazy_re_compile(
        r'(\w+\.)\w+', re.IGNORECASE
    )

validate_email = CustomEmailValidator()