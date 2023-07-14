from django.urls import path
from weather_app.views import weather_forecast


urlpatterns = [
    path('api/weather/<float:latitude>/<float:longitude>/<str:detailing_type>/', weather_forecast, name='weather_forecast'),
]
