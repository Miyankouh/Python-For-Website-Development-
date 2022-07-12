from django.core.exceptions import ValidationError


def min_length_validators(value):
    if len(value) != 16:
        raise ValidationError("Length is not 16")