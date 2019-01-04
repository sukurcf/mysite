from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

gender_choice = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Tenant(models.Model):
    name = models.CharField(max_length = 30, blank=False)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)], blank=False)
    gender = models.CharField(max_length=6, choices=gender_choice, blank=False)
    mobile_1 = PhoneNumberField(null=False, blank=False, unique=True)
    mobile_2 = PhoneNumberField(null=False, blank=False, unique=True)
    mobile_3 = PhoneNumberField(null=False, blank=False, unique=True)
    address_1 = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=20, blank=False)
    country = CountryField(blank=False)
    location = models.CharField(max_length=20, blank=False)
