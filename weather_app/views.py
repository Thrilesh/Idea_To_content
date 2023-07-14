from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import WeatherForecast
from datetime import datetime, timedelta
import requests

def is_data_relevant(timestamp):
    # Get the current time
    current_time = datetime.now()

    # Calculate the time difference between the current time and the timestamp
    time_difference = current_time - timestamp

    # Define the relevance threshold (10 minutes in this case)
    relevance_threshold = timedelta(minutes=10)

    # Check if the time difference is within the relevance threshold
    return time_difference <= relevance_threshold

def weather_forecast(request, latitude, longitude, detailing_type):
    # Check if data exists in the local database and is still relevant
    weather_forecast = get_object_or_404(
        WeatherForecast,
        latitude=latitude,
        longitude=longitude,
        detailing_type=detailing_type
    )

    # Check if the stored data is still relevant based on the timestamp
    if not is_data_relevant(weather_forecast.timestamp):
        # Make a request to OpenWeatherMap API
        api_key = "4cd3856ba389baf8381ff8a547b41b3a"  
        api_url = f"https://api.openweathermap.org/data/2.5/{detailing_type}"
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": api_key
        }
        response = requests.get(api_url, params=params)

        if response.ok:
            # Update the local database with the new forecast data
            weather_forecast.forecast_data = response.json()
            weather_forecast.save()

    # Return the weather forecast data in the API response
    return JsonResponse({
        "latitude": weather_forecast.latitude,
        "longitude": weather_forecast.longitude,
        "detailing_type": weather_forecast.detailing_type,
        "forecast_data": weather_forecast.forecast_data,
        "timestamp": weather_forecast.timestamp
    })
