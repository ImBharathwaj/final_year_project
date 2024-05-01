import requests
import http
import os

def extract():
    api_key = "5740b0812c744b519ae63746240105"
    cities = ["Chennai", "Mumbai", "Bangalore", "Hyderabad", "Kolkata", "Cochin"]
    f = open("data.json", "a")
    f.write("[")
    d = len(cities)
    for city in cities:
        d -= 1
        res = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"
        )
        # print(res.headers['content-type'])
        # print(res.json())
        if d > 0:
            f.writelines(f"{res.text},\n")
        else:
            f.writelines(f"{res.text}")
        print("Writing json completed")
    f.write("]")
    f.close()
