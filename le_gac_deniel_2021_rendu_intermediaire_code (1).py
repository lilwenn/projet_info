#IMPORTATIONS

import json
import urllib
import matplotlib.pyplot as plt
import numpy as np

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

#etape 3
def moyenne(list,nb_valeurs):
    """
    Fonction permettant de calculer la moyenne d'une liste donnée
    @param list: liste des données météorologiques
    @return moyenne: retourne la moyenne des valeurs
    """
    somme=0
    for valeur in list:
        somme += valeur
    moyenne = somme / nb_valeurs
    return round(moyenne, 2)  
    
#calcul écart-type
def ecart_type(list,nb_valeurs): 
    """
    Fonction permettant de calculer l'écart type d'une liste donnée
    @param list: liste des données météorologiques
    @return ecart-type: retourne l'écart-type des valeurs
    """
    #somme valeurs au carré 
    somme_carre = 0
    for valeur in list:
        somme_carre += (valeur - moyenne(list,nb_valeurs))**2
    ecart_type=((somme_carre / nb_valeurs)**0.5)
    return round(ecart_type,2)

#calcul de la médiane
def tri_croissant(liste_croissante):
    """
    Fonction permettant de trier les valeurs d'une liste par ordre croissant
    @param liste_croissante: liste des données météorologiques
    """
    permutation = True
    i = 0
    while permutation:
        permutation = False
        for elem in liste_croissante:
            if i < len(liste_croissante)-1:
                if liste_croissante[i] > liste_croissante[i+1]:
                    # Echange de valeurs
                    liste_croissante[i+1], liste_croissante[i] = liste_croissante[i], liste_croissante[i+1]
                    permutation = True
            i += 1
        i = 0

def mediane(liste_croissante):
    """    
    Fonction permettant de calculer la médiane d'une liste donnée
    @param liste_croissante: liste des données météorologiques
    @return mediane: retourne l'écart-type des valeurs
    """
    tri_croissant(liste_croissante)
    lg_liste_croissante = len(liste_croissante)
    if lg_liste_croissante == 0:
        return None
    if lg_liste_croissante == 1:
        mediane=liste_croissante[0]
        return mediane
    
    i = int(lg_liste_croissante / 2)
    if lg_liste_croissante % 2 == 0:  # Nb pair d'éléments
        mediane=(liste_croissante[i-1] + liste_croissante[i])/2
        return mediane
    mediane=liste_croissante[i]
    return mediane

#calcul pourcentage minimal et maximal 
def valeur_min_max(list):
    """    
    Fonction permettant de trouver la valeur maximale d'une liste donnée
    @param  list: liste des données météorologiques
    @return valeur_min : retourne la plus petite valeur
    @return valeur_min : retourne la plus grande valeur
    """
    val_min = list[0]
    i = 1
    while i < len(list):
        if list[i] < val_min:
            val_min = list[i]  
        i += 1
    

    val_max = list[0]
    i = 1
    while i < len(list):
        if list[i] > val_max:
            val_max = list[i]
        i += 1
    return[val_min,val_max]
    
    
#graphiques

def graphe (list,heures) :
    """
    Fonction permettant de créer une courbe
    @param heures : liste des heures comprises entre 4h et 22h (exclue)
    @param list: liste des données météorologiques 
    @return plt.show(): graphique du pourcentage de nébulosité en fonction des heures
    """
    plt.plot (heures,list)
    plt.ylabel('Nébulosité (%)')
    
    plt.xlabel('Temps (en heures)')
    plt.title('Courbe de la nébulosité en fonction des heures du 24/06/21 à Brest')
    return plt.show()


def histogramme(list,heures):
    """
    Fonction permettant de créer un histogramme
    @param list: liste des données météorologiques 
    @param heures : liste des heures comprises entre 4h et 22h (exclue)
    @return plt.show(): histogramme des heures en fonction du pourcentage de nébulosité
    """ 
    
    plt.rcdefaults()
    fig, ax = plt.subplots()
    
    y_pos = np.arange(len(heures))
     
    ax.barh(y_pos, list, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(heures)  
    plt.ylabel('Temps (en heures)')
    ax.set_xlabel('Pourcentage de nuages (%)')
    ax.set_title('Histogramme des heures en fonction du pourcentage de nébulosité du 24/06/21 à Brest')
    
    return (plt.show())
    
#PROGRAMME PRINCIPAL

#etape1 : sauvegarde données JSON dans fichier et chargement de ces données dans python 
print("")
print("Etape 1 : Sauvegarde des données du site dans un fichier + dans un dictionnaire python")

#Coordonnées de Brest en France  
lat=48.3897
lon=-4.48333

heure_demandee=1624500000   
key = "96d573b1b230d017de8d54326c23c640"
lien = f" https://api.openweathermap.org/data/2.5/onecall/timemachine?q=Brest&dt={heure_demandee}&appid={key}"

print(lien)

#Boucle du 24/06/2021 de 4h à 22h à Brest
dico_24_06={}
filename="fichier_donnees"
list=[]
  
#Chercher données sur le site
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

print("")
print("--------------------------------------------------------------------------")
print("Etape 2 : Récupération des données entre 4h et 22h (exclue) ")
print("")
heure=4
while heure<22:  
#Mettre en liste le pourcentage de couverture nuageuse
    list.append(dico_24_06[str(heure_demandee)]["hourly"][heure]["clouds"])
    heure+=1
print(f"Pourcentage de couverture nuageuse : {list}")

#etape 3 
print("")
print("-------------------------------------------------------------------------")
print("Etape3 : Traitements statistiques des données météorologiques")
print("")
nb_valeurs = len(list)
print(f"La moyenne est de {moyenne(list,nb_valeurs)} %")
print(f"L'écart-type est de {ecart_type(list,nb_valeurs)}") 

#calcul de la médiane:
#tri de la liste par ordre croissant 
liste_croissante=[]  
for nb in list:
    liste_croissante.append(nb)

print(f"La mediane est de {mediane(liste_croissante)} %") 
print(f"Le pourcentage minimal de nébulosité est de {valeur_min_max(list)[0]} %")
print(f"Le pourcentage maximal est de nébulosité est de {valeur_min_max(list)[1]} %")

#etape 4
print("")
print("------------------------------------------------------------------")
print("Etape 4 : cf graphiques ")

crenaux_heures=[]
h=4
while h<22:
    crenaux_heures.append(h)
    h+=1

graphe(list,crenaux_heures)
histogramme(list,crenaux_heures)










