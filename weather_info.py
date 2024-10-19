import requests

def weather(place):
    api_key = '7740b4a853b86766dd275cf42b57d7dd'  
    base_url = "https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=27.6883&lon=85.3263&zoom=5"
    
   
    url = f"{base_url}q={place}&appid={api_key}&units=metric"
    
    # Send the request to the OpenWeatherMap API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return
    
    # Parse the JSON response
    data = response.json()
    
    if data["cod"] != 200:
        print(f"City {place} not found!")
        return
    
    # Extract the relevant weather data
    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    # Display the weather information
    print(f"Weather in {place}:\nTemperature: {temp}°C\nCondition: {condition}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")

# Example usage:
city = input("Enter city name: ")
weather(city)
