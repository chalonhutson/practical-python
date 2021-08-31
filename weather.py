import requests

def get_weather_desc_and_temp():
    api_key = "65c6ea521df7d140c62eface31665755"
    city = "Philadelphia"
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=imperial".format(city_name = city, API = api_key)

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"description": description,
        "temp_min": temp_min,
        "temp_max": temp_max}


def main():
    weather_dict = get_weather_desc_and_temp()
    # Print the results
    print("Today's forcast is", weather_dict.get("description"))
    print("The minimum temperature is", weather_dict.get("temp_min"), "degrees.")
    print("The maximum temperature is", weather_dict.get("temp_max"), "degrees.")

main()