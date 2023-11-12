# Dashboard sur les apparitions d'UFOs depuis 1910

Ce dashboard a été réalisé par Timothée DUMAS dans le cadre de l'unité 23_E4_DSIA_4101A - Python pour la datascience

## La base de données (https://www.kaggle.com/datasets/jonwright13/ufo-sightings-around-the-world-better)

La base de données contient des informations sur les UFOs (objets volants non identifiés) recensés entre 1910 et 2014. L'organisation qui à produit ce jeu de donnée est NUFORC. Les colonnes présentes dans le CSV téléchargé sont : 
- Date_time
- date_documented
- Year
- Month
- Hour
- Season 
- Country_Code
- Country
- Region
-  Locale
- latitude
- longitude
- UFO_shape
- length_of_encounter_seconds
- Encounter_Duration,
- Description

dans ce projet j'utilise un fichier cleandata.csv qui est deja nettoyé. le code clean.py utilisé pour le nettoyage est visible dans le projet R.

## User Guide

Le but de ce projet est d'analyser et de visualiser les données collectées par la NUFORC. 

### Installation 

ouvrir un terminal sur votre machine locale et placer vous dans le répertoire souhaité puis taper cette liste de commandes  :

- git clone https://github.com/timotheedumas/23_E4_DSIA_4101A_projet_python.git # pour cloner le répertoire git sur votre machine
 
Avant de continuer vérifier à l'aide votre explorateur de fichiers que tout les fichiers ont bien tous été téléchargés dans le même dossier. 

- Ouvrez vs code
- Installer les packages listés dans le requirement.txt
- run le programme pour ouvrir le dashboard.


### Utilisation

un curseur en haut de la page permet de changer la date de tout les graphiques, sauf la premère courbe qui est statique.

Sur la carte il est possible de passer la souris sur les differents points pour afficher une infobulle contenant des informations sur l'ufo.


## Analyse des résultats


- Graphique du nombre d'UFO par an :
Le nombre d'UFO recensés augmente au cours des années, notamment autour des années 2000 où l'émergence d'Internet a favorisé les théories du complot. La forte baisse du nombre de données en 2014 est simplement due au fait que la base de données a été constituée au milieu de l'année 2014 et donc il n'y a que la moitié de l'année de représentée.

- Histogramme sur la durée d'apparition :
La plupart des apparitions durent entre 10 secondes et 30 minutes (surtout entre 1 et 5 minutes).

- Camembert sur les saisons :
Les UFOs sont plus souvent observés en été, beaucoup moins en hiver. Les extraterrestres seraient-ils frileux ? Ou simplement le ciel est plus dégagé en été donc les objets volants sont plus visibles.

- Camembert sur les formes d'UFO :
Ce graphique montre que les formes prédominantes sont circulaires (cercle, disque, ovale...), triangulaires et lumineuses.

- Répartition des UFO dans le monde :
La plupart des UFOs sont observés dans les pays anglophones tels que les États-Unis, l'Angleterre, l'Inde et l'Australie, probablement car "UFO" est un terme anglais. L'écrasante majorité des données sont recensées aux États-Unis, peut-être parce que la culture de l'UFO y est plus répandue, ou peut-être parce que les aliens sont des amateurs de cheeseburgers ? Il est aussi possible ce soit parce que l'organisation productrice de ces données est américaine et donc il lui est donc plus facile de collecter des données.