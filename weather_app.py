import json
import requests

query = input("Enter Your City Country or Country Name : " )
url = "http://api.weatherapi.com/v1/current.json?key=1b5144912d694ca2ba575632233007&q="


try:
    req = url+query
    r = requests.get(req, timeout=10)
    r.raise_for_status()
except requests.exceptions.Timeout:
    print("Your internet is slow.")
except requests.exceptions.RequestException as e:
    print("Request failed:", e)


if '{"error":{"code":1006,"message":"No matching location found."}}' in r.text:
    print("Unknown City or Country.")
else:
    wdic = json.loads(r.text)
    temp_c = (wdic["current"]["temp_c"])
    temp_f = (wdic["current"]["temp_f"])
    country = (wdic["location"]["country"])
    localtime = (wdic["location"]["localtime"])
    condition = (wdic["current"]["condition"]["text"])
    wind_mph = (wdic["current"]["wind_mph"])
    wind_kph = (wdic["current"]["wind_kph"])
    wind_dir = (wdic["current"]["wind_dir"]) 
    humidity = (wdic["current"]["humidity"])
    temp_c = (f"Temperature of {query.title()} : {temp_c}℃  & {temp_f}℉")
    print(temp_c)
    print(f"Country : {country}")
    print(f"Time : {localtime}")
    print(f"Condition : {condition}")
    print(f"Wind : {wind_mph}mph {wind_kph}kph Direction of Wind {wind_dir}")
    print(f"Humidity : {humidity}")
