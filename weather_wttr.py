import requests


cities = ["Лондон", "Череповец", "Шереметьево"]
wind_speed = "?M"
narrow_format = "?n"
quiet_format = "?q"
bl_wt = "?T"
city_one = "Череповец"




def three_cities(cities):

    url = "http://ru.wttr.in/"
    for i in cities:
        url_address = url + i
        response = requests.get(url_address)
        print(response.text)


def weather_cherepovets(city_one, wind_speed):
    url = "https://ru.wttr.in/"
    url_address = url + city_one + wind_speed
    response = requests.get(url_address)
    print(response.text)


def narrow_weather_cherepovets(city_one, wind_speed, narrow_format):
    url = "https://ru.wttr.in/"
    url_address = url + city_one + wind_speed + narrow_format
    response = requests.get(url_address)
    print(response.text)

def quiet_weather_bl_wt(city_one, wind_speed, quiet_format, bl_wt):
    url = "https://ru.wttr.in/"
    url_address = url + city_one + wind_speed + quiet_format + bl_wt
    response = requests.get(url_address)
    print(response.text)

def main():
    quiet_weather_bl_wt(city_one, wind_speed, quiet_format, bl_wt)


if __name__ == "__main__":
    main()

