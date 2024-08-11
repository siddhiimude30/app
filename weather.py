import requests

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
API_KEY = 'your_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """Fetches the weather information for a given city."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        city_name = data['name']
        temperature = main['temp']
        weather_description = weather['description']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather_description.capitalize()}")
    else:
        print("City not found or API request failed.")

def main():
    print("Welcome to the Weather Forecast App!")
    city = input("Enter the city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
