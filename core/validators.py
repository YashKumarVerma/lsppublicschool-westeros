from django.core import validators

from westeros.settings.configuration import (
    MAXIMUM_USERNAME_LENGTH,
    MINIMUM_USERNAME_LENGTH,
)


class UsernameValidator(validators.RegexValidator):
    regex = fr"^[\w.-]{{{MINIMUM_USERNAME_LENGTH},{MAXIMUM_USERNAME_LENGTH}}}$"
    message = "Enter a valid username. This value may contain only letters, numbers, and . - _ characters."
    flags = 0
