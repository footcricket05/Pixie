#TheWeather
from requests import get
from json import loads
try:
    from weather import Weather, Unit
except:
    print("Please install weather-api!")
def TheWeather():
    response = get("http://ipinfo.io/json")
    responseDecode = loads(response.text)
    latlon = responseDecode["loc"].split(",")
    weather = Weather(unit=Unit.CELSIUS)
    lookup = weather.lookup_by_latlng(latlon[0], latlon[1])
    condition = lookup.condition
    #print("Currently, in " + responseDecode["city"] + " it is " + condition.temp + " degrees")
    return("Currently, in " + responseDecode["city"] + " it is " + condition.temp + " degrees")
