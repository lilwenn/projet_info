import json
import urllib

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

#coordonées Brest en France  
lat=48.3897
lon=-4.48333

heure_demandee=1624500000
key = "96d573b1b230d017de8d54326c23c640"  #entrez votre clé OpenWeatherMap
#lien = f"https://api.openweathermap.org/data/2.5/onecall/timemachine/weather?lat={lat}&lon={lon}&dt={heure_demandee}&appid={key}"
lien = f" https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={heure_demandee}&appid={key}"
#lien=f"https://api.openweathermap.org/data/2.5/weather?q=Brest&dt={heure_demandee}&appid={key}"
print(lien)

#Boucle du 24/06/2021 de 4h à 22h
dico_24_06={}
filename="fichier_donnees"
list=[]

  
#Chercher données sur le site (fonction 1)
url = urllib.request.urlopen(lien) #execution de la requête
donnees = json.loads(url.read().decode())#recuperation des données

#verif: print(donnees)

#Mettre dans un fichier (fonction 2)

save_weather_data(donnees, filename)

#fichier dans Python

dico_24_06[str(heure_demandee)]=load_weather_data(filename)

print(dico_24_06)
heure=4

while heure<22:
    
#Mettre en liste le pourcentage de nuages
    list.append(dico_24_06[str(heure_demandee)]["hourly"][heure]["clouds"])
    heure+=1

print(list)

"""
#moyenne
somme=0
i=0
while i<len(list):
    somme+=i
    i+=1
moy=somme/len(list)
print(moy)


def mediane(list):
    i=1
    val_max=list[0]
    val_min=list[0]
    for i in list:
        if i+1 < val_min:
            val_max=i
        if i+1 > val_m:
            val_min=i
        i+=1
    print(val_min)
    print(val_max)
    med=(val_max-val_min)/2
    return med
"""
def moyenne(list):
    moy=0
    for i in list:
        moy+=i
    moy=moy/len(list)
    return moy

def variance(list):
    var=0
    moy=moyenne(list)
    for i in list:
        a=(i-moy)*(i-moy)
        var+=a
    var=var/(len(list)-1)
    return var

def ecart_type(list):
    var=variance(list)
    var=var/len(list)
    ecart_tp=var**0.5
    return ecart_tp

#print(mediane(list))
print(moyenne(list))
print(variance(list))
print(ecart_type(list))

