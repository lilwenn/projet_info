import json
import urllib
#import matplotlib.pyplot as plt
#import numpy as np

#FONCTIONS
#etape 1
def save_weather_data(donnees, filename):
	"""
	Fonction permettant de sauvegarder des données JSON dans un fichier
	:param dict data : contient dans un dictionnaire les données JSON
	:param string filename : le nom du fichier de sauvegarde
	"""
	file_handle = open(filename, "w")
	json.dump(donnees, file_handle)
	file_handle.close()
    
def load_weather_data(filename):
	"""
	Fonction permettant de charger des données JSON à partir d'un fichier
	:param string filename : le nom du fichier de sauvegarde
	:return dict data : retourne le dictionnaire des données du fichier
	au format JSON
	"""
	file_handle = open(filename, "r")
	data = json.load(file_handle)
	file_handle.close()
	return data

    
#PROGRAMME PRINCIPAL
#etape1 : sauvegarde données JSON dans fichier et chargement de ces données dans python
print("")
print("Etape 1 : Sauvegarde des données du site dans un fichier + dans un dictionnaire python")

#Coordonnées de Brest en France  
lat=48.3897
lon=-4.48333

heure_demandee=1624500000   
key = "96d573b1b230d017de8d54326c23c640"
#lien = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&units=metric&appid={key}"

#Boucle du 24/06/2021 de 4h à 22h à Brest
dico_24_06={}
filename="fichier_donnees"
list=[]
capitales=["Paris","Dublin","Madid","Lisbonne","Amsterdam","Bruxelle","Luxembourg","Rome","Vienne","Prague","Ljubjana","Berlin","Copenague","Varsovie","Bratislava,Budapeste","Bucarest","Sophia","Zagreb","Riga","Vilrius","Tallinn","Helsinki","Athènes","La Valette","Nicosie"]
for ville in capitales:
    #Chercher données sur le site
    lien = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&units=metric&appid={key}"
    url = urllib.request.urlopen(lien) #execution de la requête
    donnees = json.loads(url.read().decode())#recuperation des données
    #Mettre dans un fichier (fonction 1)
    save_weather_data(donnees, filename)
    #Transférer les données du fichier dans Python (fonction 2)
    dico_24_06[str(heure_demandee)]=load_weather_data(filename)
    print("")
    print("Voici les données météorologiques du Jeudi 24/06/21 à Brest :")
    print("")
    print(dico_24_06)

 #etape 2
"""
    print("")
    print("--------------------------------------------------------------------------")
    print("Etape 2 : Récupération des données entre 4h et 22h (exclue) ")
    print("")
    heure=4
    while heure<22:  
    #Mettre en liste le pourcentage de couverture nuageuse
        list.append(dico_24_06[str(heure_demandee)]["hourly"][heure]["temp"])
        heure+=1
    print(f"Pourcentage de couverture nuageuse : {list}")"""
