# 2022-2023-4gp-Alméras-Lisoir

1. Contexte du projet

Ce projet s'inscrit au sein de l'unité de formation "Du capteur au banc de test en open source hardware". Ce cours est dispensé en quatrième année au sein du département de Génie Physique de l'INSA Toulouse.
Ce projet s'étend sur le deuxième semestre de l'année 2022-2023 et a pour but de nous sensibiliser aux différentes étapes de conception et d'analyse pour l'utilisation d'un capteur.


2. Caractéristiques et travaux de recherche préliminaires sur le capteur

Le capteur sur lequel nous avons mené nos recherches est un exemple de technologie low-tech. En effet, un article scientifique publié en 2014 met en évidence que du graphite déposé sur une bande de papier peut servir de jauge de contrainte. Le projet Capteur s'inspire largement des études et expériences présentées dans ce papier.
"faire un résumé du papier et des explications physiques". 


3. Cours et formation

Pour mener ce projet, nous avons d'abord suivi différents cours et TPs
- Introduction à la chaîne de mesure
- TP développement d'un capteur à jauge de contrainte à base de crayon graphite
- TP conception d'un circuit analogique pour interfacer le capteur à jauge de contrainte
- TP programmation de microcontrôleurs et au développement d'un matériel open source,
- TP shield électronique PCB dédié à l'interface du capteur de contrainte,
- TP consacrés à la réalisation du banc de test de la jauge de contrainte,
- Coursa fiche technique de la jauge de contrainte
- Cours Github

<img width="402" alt="image" src="https://user-images.githubusercontent.com/124165435/232909479-6e11000b-4ce8-4656-aaaf-82b67eb49942.png">


4. Livrables initiales du projet
Le shield PCB
Un shield PCB devra être designé et fabriqué. Il sera ensuite connecté à une plaque Arduino UNO. Le shield doit contenir au minimum un amplificateur transimpédence, un module Bluetooth, et si possible un écran OLED et un encodeur rotatoire pour la calibration du capteur.

La carte Arduino UNO 
La carte Arduino fonctionnera avec un code permettant de mesurer la containte appliquée sur le capteur. Si besoin, la carte devra aussi contrôler le module Bluetooth, l'écran OLED et l'encodeur rotatoire.

Une application Android APK
Un protocole de test
La datasheet du capteur de déformation

Révisions des livrables du projet
Notre binôme ne possède aucun téléphone Android et il n'était donc pas possible de créere une application APK et de transmettre les données par Bluetooth. Nous avons du rediscuter les livrables avc nos responsables de projet.

Au lieu de fournir une application Android APK, nous développons une interface en Python. Cette interface permet la réception des données envoyées par la carte Arduino, via une communication en RS-232 entre un ordianteur et la carte.


