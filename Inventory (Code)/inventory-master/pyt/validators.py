from django.core.exceptions import ValidationError
import datetime

def nonneg(value):
    if value<0:
        raise ValidationError('Input can not be negative')

from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Invalid Name')
phoneno= RegexValidator(r'^[a-zA-Z]*$', '')

def datevalid(value):
    if value > datetime.date.today():
        raise ValidationError("The date can not be in future")
    return value