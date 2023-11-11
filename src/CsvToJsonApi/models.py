from django.db import models

class WeatherData(models.Model):
    date = models.CharField(max_length=10)
    precipitation = models.FloatField()
    temp_max = models.FloatField()
    temp_min = models.FloatField()
    wind = models.FloatField()
    weather = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.date} - {self.weather}"