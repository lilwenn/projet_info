#2 Récupération des données
#2.1 Lecture de données au format JSON

import json
json_file = open("my_data.json") #ce fichier est dans le répertoire de travail
data = json.load(json_file) #on lit les données et on les stocke dans data
json_file.close() #on ferme le fichier
#la variable 

import json
with open("my_data.json") as json_file:
    data = json.load(json_file)
print(data)

#2.3 Récupération des données avec Python

import urllib
key = "96d573b1b230d017de8d54326c23c640" #entrez votre clé OpenWeatherMap
myrequest = "https://api.openweathermap.org/data/2.5/weather?q=Paris&appid="+key
url = urllib.request.urlopen(myrequest) #execution de la requête
data = json.loads(url.read().decode()) #recuperation des données
print(data) #affichage des données

#2.3 Récupération des données avec Python en Celsius


import urllib
key = "96d573b1b230d017de8d54326c23c640"  #entrez votre clé OpenWeatherMap
myrequest = "https://api.openweathermap.org/data/2.5/weather?q=Paris&units=metric&appid="+key
url = urllib.request.urlopen(myrequest) #execution de la requête
data = json.loads(url.read().decode()) #recuperation des données
print(data) #affichage des données

#2.4 Sauvegarde des données JSON dans un fichier avec Python

file_handle = open("dataSaved.json", "w")
json.dump(data, file_handle)
file_handle.close()

#2.5 Lecture des données JSON contenues dans un fichier avec Python

file_handle = open("dataSaved.json", "r")
data = json.load(file_handle)
file_handle.close()

#3 Format des heures/dates
#3.1 Le module datetime

from datetime import datetime
    # date courante
now = datetime.now()
print('Now :', now)
print('Now (formaté):', now.strftime("%d/%m/%Y %Hh%M"))
print('Now infos :', now.year, now.month, now.day, now.hour, now.minute,
now.second)
print('Now dt :', now.timestamp())
    # date donnée
holidays = datetime(2021, 7, 2, 18, 0, 0)
print('Vacances :', holidays)

#3.2 Le timestamp
#convertir un timestamp en une date lisible:
from datetime import datetime
timestamp = 1619136000
print('date :', datetime.fromtimestamp(timestamp))

# récupérer la date d’aujourd’hui dans un format timestamp :
    
from datetime import datetime
now = datetime.now()
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

#4 Pour bien démarrer
