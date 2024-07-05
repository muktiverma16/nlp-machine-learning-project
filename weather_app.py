import requests
import json
 
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

city=input("Enter city name")
url=f"https://api.weatherapi.com/v1/current.json?key=44d51f55184b4e8abc072911242905&q={city}"
r=requests.get(url)
#print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")

text="the current weather in {city} is {w} degrees."
speak.Speak(f"the current weather in {city} is {w} degrees.")
