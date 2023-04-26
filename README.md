# 2022-2023-4gp-Alméras-Lisoir

## Sommaire
* [1. Description du projet](#PremiereSection)
  * [1.1. Caractéristiques et travaux de recherche préliminaires sur le capteur](#PremiereSection1)
  * [1.2. Cours et formation](#PremiereSection2)
* [2. Livrables](#DeuxiemeSection)
  * [2.1. Livrables initiaux](#DeuxiemeSection1)
  * [2.2. Rediscussion des attentes](#DeuxiemeSection2)
* [3. Arduino](#TroisiemeSection)
* [4. KiCad](#QuatriemeSection)
  * [4.1. Symboles et empreintes des composants](#QuatriemeSection1)
  * [4.2. Schématique](#QuatriemeSection2)
  * [4.3. Placement des composants](#QuatriemeSection3)
  * [4.4. Visualisation 3D](#QuatriemeSection4)
* [5. Fabrication du shield](#CinquiemeSection)
  * [5.1. Réalisation du PCB](#CinquiemeSection1)
  * [5.2. Perçage et soudure](#CinquiemeSection2)
* [6. Développement de l'interface en Python](#SixiemeSection)
* [7. Simulation avec LTSpice](#SeptiemeSection)
* [8. Tests et résultats](#HuitiemeSection)
  * [8.1. Banc de test](#HuitiemeSection1)
  * [8.2. Résultats obtenus](#HuitiemeSection2)
  * [8.3. Analyse des résultats et pistes d'améliorations](#HuitiemeSection3)
* [9. Datasheet](#NeuviemeSection)
* [Contacts](#DixiemeSection)


## 1. Description du projet <a id="PremiereSection"></a>

Ce projet s'inscrit au sein de l'unité de formation "Du capteur au banc de test en open source hardware". Ce cours est dispensé en quatrième année au sein du département de Génie Physique de l'INSA Toulouse.
Ce projet s'étend sur le deuxième semestre de l'année 2022-2023 et a pour but de nous sensibiliser aux différentes étapes de conception et d'analyse pour l'utilisation d'un capteur.


## 1.1 Caractéristiques et travaux de recherche préliminaires sur le capteur <a id="PremiereSection1"></a>

Le capteur sur lequel nous avons mené nos recherches est un exemple de technologie low-tech. En effet, un article scientifique publié en 2014 met en évidence que du graphite déposé sur une bande de papier peut servir de jauge de contrainte. Le projet Capteur s'inspire largement des études et expériences présentées dans ce papier.
"faire un résumé du papier et des explications physiques". 


## 1.2 Cours et formation <a id="PremiereSection2"></a>

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


## 2. Livrables du projet <a id="DeuxièmeSection"></a>

## 2.1 Livrables initiaux <a id="DeuxièmeSection1"></a>

* Le shield PCB
Un shield PCB devra être designé et fabriqué. Il sera ensuite connecté à une plaque Arduino UNO. Le shield doit contenir au minimum un amplificateur transimpédence, un module Bluetooth, et si possible un écran OLED et un encodeur rotatoire pour la calibration du capteur.

* La carte Arduino UNO 
La carte Arduino fonctionnera avec un code permettant de mesurer la containte appliquée sur le capteur. Si besoin, la carte devra aussi contrôler le module Bluetooth, l'écran OLED et l'encodeur rotatoire.

* Une application Android APK
* Un protocole de test
* La datasheet du capteur de déformation

## 2.2 Révisions des livrables du projet <a id="DeuxièmeSection2"></a>
Notre binôme ne possède aucun téléphone Android et il n'était donc pas possible de créere une application APK et de transmettre les données par Bluetooth. Nous avons du rediscuter les livrables avc nos responsables de projet. Finalement, nous développons une interface en Python. Cette interface permet la réception des données envoyées par la carte Arduino, via une communication en RS-232 entre un ordinateur et la carte.

## 3. Carte Arduino UNO et code associé <a id="TroisièmeSection"></a>

Le code Arduino que nous avons écrit

## 4. KiCad <a id="QuatriemeSection"></a>

### 4.1. Symboles et empreintes des composants <a id="QuatriemeSection1"></a>
* Amplificateur LTC1050
* Ecran OLED

### 4.2. Schématique <a id="QuatriemeSection2"></a>

### 4.3. Placement des composants <a id="QuatriemeSection3"></a>
 
### 4.4. Visualisation 3D <a id="QuatriemeSection4"></a>

## 5. Fabrication du shield <a id="CinquiemeSection"></a>
### 5.1 Réalisation du PCB <a id="CinquiemeSection1"></a>
"expliquer le process fait avec Cathy"
## 5.2 Perçage et soudure <a id="CinquiemeSection2"></a>
"mettre des petites photos"

## 6. Développement de l'interface en Python <a id="SixiemeSection"></a>
L'interface développée répond à plusieurs problématiques et présente différentes fonctionnalités.
- Connexion automatique au port utilisé par la connexion avec l'Arduino (message pop-up selon le succès de la connection au port)
- Etape préliminaire de calibration du capteur graphite
- Affichage de deux graphiques défilant exprimant la variation de la résistance du flex sensor et du capteur graphite
- Relecture et affichage en temps réel des données reçues pour les deux capteurs
- Fermeture de la fenêtre et interruption de la communication avec le bouton Quit


## 7. Tests et résultats
### 7.1 Banc de test
Pour produire notre data sheet, nous avons décidé de relever la résistance des deux capteurs pour différents angles de courbure.
### 7.2 Résultats obtenus et analyse
### 7.3 Regard critique sur les résultats

## 8. Datasheet
