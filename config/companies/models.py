from django.db import models
from navigation.models import Location

class Facility(models.Model):

    LOCATION_TYPES = [
        ("CANTEEN", "Canteen"),
        ("LIBRARY", "Library"),
        ("TOILET", "Toilet"),
    ]

    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
    ]

    name = models.CharField(max_length=100)
    location_type = models.CharField(max_length=20, choices=LOCATION_TYPES)

    block = models.CharField(max_length=10)
    floor = models.IntegerField()
    room_number = models.CharField(max_length=10, blank=True, null=True)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)

    # External company page (optional)
    profile_url = models.URLField(blank=True)

    # Optional text JD (summary / fallback)
    jd = models.TextField(blank=True)

    # Optional JD PDF (main JD source)
    jd_file = models.FileField(
        upload_to='jd_files/',
        blank=True,
        null=True
    )

    # Location-related fields
    room_number = models.CharField(max_length=20)

    venue = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'location_type': 'VENUE'}
    )

    block = models.CharField(max_length=50)
    floor = models.CharField(max_length=20)
    landmark = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
