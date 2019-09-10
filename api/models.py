from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=100, decimal_places=30)
    lon = models.DecimalField(max_digits=100, decimal_places=30)

    def __str__(self):
        return self.name + "  Lat: " + str(self.lat)+ ", Lon: " + str(self.lon)
