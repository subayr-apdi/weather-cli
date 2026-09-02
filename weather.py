import requests
import os
from dotenv import load_dotenv
# Load variables from .env into environment
load_dotenv()
def weather():
      try:
                    api=os.getenv("api")
                    if api:      
                        city_name=input("enter a city name ").strip().lower()
                        url=f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api}"
                        if city_name:
                            try:
                                response=requests.get(url,timeout=10)
                                response.raise_for_status()
                                data=response.json() 
                            except requests.RequestException as error:
                                           print("Geocoding request failed:", error)
                                           return
                            if data:
                                latitude = data[0]["lat"]
                                # print(latitude)
                                longitude=data[0]["lon"]
                                # print(longatide)
                                url_1=f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api}&units=metric"
                                response=requests.get(url_1,timeout=10)
                                response.raise_for_status()
                                data=response.json() 
                                # print(data)
                                try:
                                    temperature=data["main"]["temp"]
                                    humidity=data["main"]["humidity"]
                                    wind_speed=data["wind"]["speed"]
                                    weather_description=data["weather"][0]["description"]
                                    returned_city =data["name"]
                                    print(f"your longitude is :{longitude}")
                                    print(f"your latitude is :{latitude}")
                                    print(f"your temperature is :{temperature}")
                                    print(f" your humidity :{humidity}")
                                    print(f"wind speeed is :{wind_speed}")
                                    print(f"city name :{returned_city}")
                                    print(f"weather dicrption is: {weather_description}")
                                except KeyError as error:
                                           print("Weather data is missing:", error)
                            else:
                                   print("no city that have that name plase enter a valid city name")
                        else:
                          print('Enter valid city name')
                    else:
                          print("API key is missing from the .env file")
      except requests.RequestException as error:
                    print("Request failed:", error)
weather()