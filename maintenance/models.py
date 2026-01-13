from django.db import models
from django.contrib.auth.models import User

class Maintenance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
    ]

    MAINTENANCE_CHOICES = [
        ('oil', 'Oil Change'),
        ('brake', 'Brake'),
        ('air_filter', 'Air Filter'),
    ]

    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_CHOICES)
    maintenance_type = models.CharField(max_length=20, choices=MAINTENANCE_CHOICES)
    odometer = models.IntegerField()
    date = models.DateField()

    next_service_odometer = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.maintenance_type}"
