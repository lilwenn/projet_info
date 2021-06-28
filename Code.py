import json
import urllib

#FONCTIONS

def save_weather_data(data1, filename):
    """
    Fonction permettant de sauvegarder des données JSON dans un fichier
    :param dict data : contient dans un dictionnaire les données JSON
    :param string filename : le nom du fichier de sauvegarde
    """
    file_handle = open(filename, "w")
    json.dump(data1, file_handle)
    file_handle.close()

def load_weather_data(filename):
    """
Fonction permettant de charger des données JSON à partir d'un fichier
:param string filename : le nom du fichier de sauvegarde
:return dict data :    file_handle = open(filename, "r")
    data = json.load(file_handle)
    file_handle.close()
    return data retourne le dictionnaire des données du fichier
au format JSON
    """


def mise_en_forme_date(now):
    print('Now :', now)
    print('Now (formaté):', now.strftime("%d/%m/%Y %Hh%M"))


#CODE

with open("my_data.json") as json_file:
    data1 = json.load(json_file)

#coordonées Brest en France  
lat=48.3897
lon=-4.48333

heure_demandee=1624500000
key = "96d573b1b230d017de8d54326c23c640"  #entrez votre clé OpenWeatherMap

while heure_demandee < 1624564800:
    
    lien = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&current.dt={heure_demandee}&appid={key}"
    url = urllib.request.urlopen(lien) #execution de la requête
    data1 = json.loads(url.read().decode()) #recuperation des données
    
    heure_demandee+=600
#verification :
#print(data)

#FONCTION 1

filename="dataSaved.json"
save_weather_data(data1, filename)

#FONCTION 2

print(load_weather_data(filename))

#FONCTION 3

from datetime import datetime
now = datetime.now()
mise_en_forme_date(now)