import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("API key not found. Make sure you set it correctly.")
    exit()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print("City not found or API error!")
        return

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"\n📍 City: {city.title()}")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌤️ Condition: {weather.capitalize()}")

print("=== 🌦️ Weather Dashboard ===")
while True:
    city_name = input("\nEnter a city (or 'exit' to quit): ")
    if city_name.lower() == "exit":
        print("Goodbye!")
        break
    get_weather(city_name)
