from django.db import models


class Location(models.Model):

    LOCATION_TYPES = [
        ('ENTRY', 'Entry Point'),
        ('VENUE', 'Venue / Hall'),
        ('TOILET_MEN', 'Toilet (Men)'),
        ('TOILET_WOMEN', 'Toilet (Women)'),
        ('CANTEEN', 'Canteen'),
        ('LIBRARY', 'Library'),
        ('PRINCIPAL', 'Principal Cabin'),
        ('DIRECTOR', 'Director Cabin'),
        ('HOD', 'HOD Cabin'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    location_type = models.CharField(
        max_length=20,
        choices=LOCATION_TYPES,
        default='OTHER'
    )

    block = models.CharField(max_length=50, blank=True)
    floor = models.CharField(max_length=20, blank=True)
    room_number = models.CharField(max_length=20, blank=True)
    landmark = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_location_type_display()})"


class Route(models.Model):
    from_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='routes_from'
    )
    to_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='routes_to'
    )
    directions = models.TextField()

    def __str__(self):
        return f"{self.from_location} → {self.to_location}"
