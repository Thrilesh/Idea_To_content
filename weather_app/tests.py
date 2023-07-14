from django.test import TestCase
from django.urls import reverse
from .models import WeatherForecast

class WeatherForecastTest(TestCase):
    def test_weather_forecast_api(self):
        # Create test data
        WeatherForecast.objects.create(
            latitude=33.441792,
            longitude=-94.037689,
            detailing_type='minute',
            forecast_data='...',
        )
        
        # Make a test API request
        response = self.client.get(reverse('weather_forecast', args=(33.441792, -94.037689, 'minute')))
        
        # Assert the response status code and data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['latitude'], 33.441792)
        self.assertEqual(response.json()['longitude'], -94.037689)
        # ...
