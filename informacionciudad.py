from requests import get
import json

def ciudad(ciudad):
    if ciudad == "San Juan" or ciudad == "san juan":
        ciudad="san+juan"
    elif ciudad == "San Luis" or ciudad == "san luis":
        ciudad="san+luis"
    try:
        ciudad= ciudad.lower()
        request= get(f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=metric&appid=944facd6e8c0e760c0e1c60381c12246')
        ciudad=request.json()
        longitud=ciudad['coord']["lon"]
        latitud=ciudad['coord']["lat"]
        provincia=ciudad['name']
        pais=ciudad['sys']['country']
        temperatura=ciudad['main']['temp']
        SenseT=ciudad["main"]["feels_like"]
        lista=[longitud,latitud,provincia, pais, temperatura,SenseT, True]
        return lista
    except:
        return "Ingresaste mal el nombre de la provincia"
        