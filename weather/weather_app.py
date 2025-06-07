import requests

def get_weather(city):
    API_KEY = '1dbeff26df5adbc843fbb647063e7b3e'  # Your actual API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()
        if data.get('cod') != 200:
            print(f"❌ City not found: {data.get('message')}")
            return

        temp = data['main']['temp']
        condition = data['weather'][0]['description']

        print(f"\n✅ Weather in {city.title()}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌤️ Condition: {condition.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network error: {e}")

# Main Program
city = input("Enter a city name: ")
get_weather(city)
