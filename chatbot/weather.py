import requests

class Weather:
    def __init__(self, owm_api):
        self.owm = owm_api

    def get_weather(self, lat, lon):
        url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, self.owm)
        res = requests.get(url)
        return self.__parse_weather(res.json())

    def __parse_weather(self, data):
        weather_data = {}
        if data["cod"] == 200:
            main = data["main"];
            current_temp = float(main["temp"]) - 273.15
            weather_data["temp"] = current_temp
            weather_data["city"] = data['name']
            weather_data["condition"] = data["weather"][0]["description"]
            weather_data["wind"] = data["wind"]
            weather_data["pressure"] = round(float(main["pressure"])*0.029529980164712, 2)
            weather_data["humidity"] = main["humidity"]
            return weather_data
        return None