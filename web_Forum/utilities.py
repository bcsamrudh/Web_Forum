import requests

def get_weather(city):
    Api_Key = "b68f5ec51cca3ba347b05ea44fbcb2ed"

    final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)

    result = requests.get(final_URL)
    data = result.json()

    temprature = data['main']['temp']
    cordinatelon = data['coord']['lon']
    cordinatelat = data['coord']['lat']
    
    return temprature

