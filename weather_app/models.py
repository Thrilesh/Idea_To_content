from django.db import models

class WeatherForecast(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    detailing_type = models.CharField(max_length=20)
    forecast_data = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Weather forecast for {self.latitude}, {self.longitude}"
