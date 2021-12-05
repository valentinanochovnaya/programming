from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


POSITION_CHOICES = (
    ("DevOps", "DevOps"),
    ("BE Developer", "BE Developer"),
    ("FE Developer", "FE Developer")
)


class Freelancer(models.Model):
    name = models.CharField(max_length=30, blank=False, default='')
    email = models.EmailField(max_length=254, blank=False, default='')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    availability = models.IntegerField(null=False, blank=False,
                                       validators=[MinValueValidator(1), MaxValueValidator(40)])
    salary = models.IntegerField(null=False, blank=False,
                                 validators=[MinValueValidator(1), MaxValueValidator(9999999999999999)])
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, default="DEVOPS")
