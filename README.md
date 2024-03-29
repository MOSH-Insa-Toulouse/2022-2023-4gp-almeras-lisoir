# Projet Capteur 4A Génie Physique - Nina Alméras & Emma Lisoir

## Sommaire
* [1. Description du projet](#PremiereSection)
  * [1.1. Caractéristiques et travaux de recherche préliminaires sur le capteur](#PremiereSection1)
  * [1.2. Cours et formation](#PremiereSection2)
* [2. Livrables](#DeuxiemeSection)
  * [2.1. Livrables initiaux](#DeuxiemeSection1)
  * [2.2. Révisions des livrables du projet](#DeuxiemeSection2)
* [3. Carte Arduino UNO et code associé](#TroisiemeSection)
* [4. KiCad](#QuatriemeSection)
  * [4.1. Symboles et empreintes des composants](#QuatriemeSection1)
  * [4.2. Schématique](#QuatriemeSection2)
  * [4.3. Placement des composants](#QuatriemeSection3)
  * [4.4. Visualisation 3D](#QuatriemeSection4)
* [5. Fabrication du shield](#CinquiemeSection)
  * [5.1. Réalisation du PCB](#CinquiemeSection1)
  * [5.2. Perçage et soudure](#CinquiemeSection2)
* [6. Logiciel de simulation LTSpice](#SixiemeSection)
* [7. Développement de l'interface en Python](#SeptiemeSection)
* [8. Tests et résultats](#HuitiemeSection)
  * [8.1. Banc de test](#HuitiemeSection1)
  * [8.2. Résultats obtenus et analyses](#HuitiemeSection2)
  * [8.3. Regard critique sur les résultats](#HuitiemeSection3)
* [9. Datasheet](#NeuvièmeSection)



## 1. Description du projet <a id="PremiereSection"></a>

Ce projet s'inscrit dans le cadre de l'unité de formation "Du capteur au banc de test en open source hardware". Ce cours est dispensé en quatrième année au sein du département de Génie Physique de l'INSA Toulouse.
Ce projet s'étend sur le deuxième semestre de l'année 2022-2023 et a pour but de nous sensibiliser aux différentes étapes de conception et d'analyse utiles à la création d'un capteur.


### 1.1 Caractéristiques et travaux de recherche préliminaires sur le capteur <a id="PremiereSection1"></a>

Le KTY2000 est un exemple de technologie low-tech à base de graphite. Ce projet s’inspire du travail mené par plusieurs scientifiques et publié dans [cet article](https://www.nature.com/articles/srep03812) en 2014. En effet, les études ont révélé les nombreux avantages du carbone graphite. L’électronique à base de papier attire de plus en plus les ingénieur.es de par sa facilité d’approvisionnement, de fabrication et son faible coût. Il suffit dans notre cas de déposer une fine couche de graphite sur le substrat naturellement poreux pour former la base du capteur. Les mines de crayon sont constituées de réseaux percolés de fines poudres de graphite liées entre elles par des argiles, permettant d’obtenir après dépôt de fins films conducteurs non fabriqués en laboratoire. 

Le système à l’étude est granulaire, autrement dit il existe une dépendance entre la conductivité électrique et l’espace moyen entre les nanoparticules de graphite. Ainsi, une déformation de la feuille de papier va modifier la conductivité globale de la couche de graphite, induisant des changements de résistances réversibles lors des déformations en compression ou en traction. Ceci constitue en fait le principe d'une jauge de contrainte. 
L’expérience est réalisée avec différentes duretés de mine de crayon (2H, HB, 2B). Les mesures de résistance pour chaque crayon sont réalisées en fonction de différents rayons de courbure (soit la déformation) ou de l’angle de flexion de notre capteur. Cela permet une caractérisation complète de chaque type de crayon et ainsi de notre capteur. 

Dans notre cas, les traces de crayon sont déposées sur du papier comme vu ci-dessous. Une fois colorié, le capteur est connecté à un système de mesures externe via des pinces crocodiles reliées à un PCB et branché sur une carte Arduino Uno.

<p align="center"><img width="329" alt="image" src="https://user-images.githubusercontent.com/124165435/234648698-2a138793-281e-4adf-a231-edec8a0e3931.png">

### 1.2 Cours et formation <a id="PremiereSection2"></a>

Pour mener ce projet, nous avons d'abord suivi différents cours et TPs.
- Introduction à la chaîne de mesure
- TP développement d'un capteur à jauge de contrainte à base de crayon graphite
- TP conception d'un circuit analogique pour interfacer le capteur à jauge de contrainte
- TP programmation de microcontrôleurs et développement d'un matériel open source
- TP LTSpice afin de simuler le fonctionnement du circuit électronique comprenant la jauge de contrainte
- TP shield électronique PCB dédié à l'interface du capteur de contrainte
- TP réalisation du banc de test de la jauge de contrainte
- Cours fiche technique de la jauge de contrainte
- Cours Github

<p align="center"><img width="402" alt="image" src="https://user-images.githubusercontent.com/124165435/232909479-6e11000b-4ce8-4656-aaaf-82b67eb49942.png">


## 2. Livrables du projet <a id="DeuxièmeSection"></a>

### 2.1 Livrables initiaux <a id="DeuxièmeSection1"></a>

* Un shield PCB devra être designé et fabriqué. Il sera ensuite connecté à une plaque Arduino UNO. Le shield doit contenir au minimum un amplificateur transimpédence, un module Bluetooth, et si possible un écran OLED et un encodeur rotatoire pour la calibration du capteur.

* La carte Arduino fonctionnera avec un code permettant de mesurer la containte appliquée sur le capteur. Si besoin, la carte devra aussi contrôler le module Bluetooth, l'écran OLED et l'encodeur rotatoire.

* Une application Android APK
* Un protocole de test
* La datasheet du capteur de contrainte

### 2.2 Révisions des livrables du projet <a id="DeuxièmeSection2"></a>
 
Notre binôme ne possède aucun téléphone Android et il n'était donc pas possible de créer une application APK et de transmettre les données par Bluetooth. Nous avons dû rediscuter les livrables avec nos responsables de projet. Finalement, nous développons une interface en Python et le module Bluetooth est supprimé. En effet, le code python créé permet la réception des données envoyées par la carte Arduino Uno, via une communication USB entre un ordinateur et la carte (port série). L'interface, confectionnée avec Qtdesigner, permet également la calibration du capteur graphite et respecte les livrables initiaux concernant l'affichage des valeurs (relatives ou non) de résistance de nos deux capteurs présents sur le setup : le KTY2000 et un flex-sensor de chez Spectral Symbol. Ce dernier est un capteur ayant les mêmes fonctionnalités que notre capteur graphite. Lorsque le flex-sensor est plié, sa variation de résistance suit la contrainte de flexion. De plus, un écran OLED affichera en temps réel de la résistance du capteur KTY2000 et celle du flex-sensor.


## 3. Carte Arduino UNO et code associé <a id="TroisièmeSection"></a>

Le code Arduino est consultable [ici](https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/tree/main/Arduino).
Ce code permet la réception des mesures faites par les deux capteurs, la conversion résistance-angle du flex-sensor et celle tension-résistance pour le KTY2000, la gestion de l'affichage sur l'écran OLED et l'envoi de données via un port série.

 
## 4. KiCad <a id="QuatriemeSection"></a>

Voici la liste des différents composants présents sur notre PCB :

- _x2 résistance 100kΩ_
- _x2 résistance 10kΩ_
- _x2 résistance 1kΩ_
- _x1 capacité 1μF_
- _x2 capacité 100nF_
- _x1 amplificateur opérationnel LTC1050_
- _x1 écran OLED I2C 0.91_

### 4.1. Symboles et empreintes des composants <a id="QuatriemeSection1"></a>
 
* Amplificateur LTC1050
* Ecran OLED
* Flex sensor

### 4.2. Schématique <a id="QuatriemeSection2"></a>
 
<p align="center"><img width="700" alt="image" src="https://user-images.githubusercontent.com/124165435/234853183-e293a26c-0e21-4e3e-af6e-2de6d5d85f0d.png">

* Amplificateur LTC1050
 
<img width="200" alt="image" src="https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/assets/124166161/4e699e19-4f88-4130-a412-251529f5d3c9"> <img width="200" alt="image" src="https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/assets/124166161/00901127-7395-493f-8a9d-51669e231fd4">

* Ecran OLED
 
<img width="300" alt="image" src="https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/assets/124166161/5af33168-c39c-4052-80d0-119bb8063c95"> <img width="200" alt="image" src="https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/assets/124166161/9bc60ae3-4dd5-4694-8d22-ddb3431aa5b5">

* Flex sensor
 
<img width="300" alt="image" src="https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/assets/124166161/e45657f0-eb76-4b49-b297-f7bdf9f01b27)">


### 4.3. Placement des composants <a id="QuatriemeSection3"></a>
 
<p align="center"><img width="448" alt="image" src="https://user-images.githubusercontent.com/124165435/234853043-2a99e37e-7576-4bbf-b96a-2a48ab394477.png">
 
### 4.4. Visualisation 3D <a id="QuatriemeSection4"></a>
 
<p align="center"><img width="350" alt="image" src="https://user-images.githubusercontent.com/124165435/234853290-a2071ead-7724-451d-831e-413aeb7c9c3b.png">


## 5. Fabrication du shield <a id="CinquiemeSection"></a>
 
### 5.1 Réalisation du PCB <a id="CinquiemeSection1"></a>

Le PCB a été fabriqué grâce au matériel mis à disposition au Génie Physique et au Génie Électrique et Informatique de l'INSA Toulouse. Les manipulations ont été faites avec l'aide de Catherine Crouzet. La modélisation du PCB fait sur [KiCad](https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/tree/main/KiCad) a été imprimée sur du papier calque tranparent. Ce motif a été ensuite transféré par UVs sur la plaquette d'epoxy finement recouverte d'une couche de cuivre. À l'aide d'un révelateur, la partie non insolée de la résine a été retirée. La plaquette d'expoxy a été ensuite placée dans un bain de perchlorure de fer pour que le cuivre non protégé par la résine soit retiré de la plaquette. Enfin, la plaque a été nettoyée des dernières traces de résine avec de l'acétone.

### 5.2 Perçage et soudure <a id="CinquiemeSection2"></a>
 
<p align="center"><img width="230" alt="image" src="https://user-images.githubusercontent.com/124166161/235507646-271bc19c-6042-436d-ab8f-c0edf065983b.png">

⌀ 0.8mm : AOP LTC1050, résistances et capacités

⌀ 1.0mm : Broches de connexion de la carte Arduino Uno

 
## 6. Logiciel de simulation LTSpice <a id="SixiemeSection"></a>
 
L'ensemble de notre circuit électronique a été simulé sur le logiciel LTSpice afin de comprendre et d'analyser son comportement dans des conditions réelles de valeurs de tension. Les différentes simulations ont permis d'une part de vérifier le bon fonctionnement du circuit et de chacun des composants intégrés, et d'autre part de comprendre l'utilité de chacun. Les images ci-dessous représentent la schématique du circuit ainsi qu'une réponse dans le temps de notre capteur à une stimulation. Se référer à la [datasheet](https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/blob/main/Datasheet/Datasheet%20KTY2000.pdf) pour de plus amples informations.
 
<p align="center"><img width="500" alt="image" src="https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/assets/124166161/034001fe-f53c-4f8f-90dd-643e3f5e0450">
<p align="center"><img width="400" alt="image" src="https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/assets/124166161/69e8a973-ebff-4334-b3cd-306d7e803378">

 
## 7. Développement de l'interface en Python <a id="SeptiemeSection"></a>
 
L'interface développée répond à plusieurs problématiques et présente différentes fonctionnalités.
- Connexion automatique au port utilisé par la connexion avec l'Arduino (message pop-up selon le succès de la connection au port)
- Étape préliminaire de calibration du capteur graphite pour l'obtension de son angle de flexion
- Relecture et affichage en temps réel des données reçues pour les deux capteurs après traitement (résistance, variation relative et angle de flexion)
- Affichage de deux graphiques défilant exprimant la variation de la résistance du flex-sensor et du capteur graphite
- Fermeture de la fenêtre et interruption de la communication avec le bouton Quit

L'apparence de l'interface a été faite avec Qt Designer. Cet outil permet de créer une interface utilisateur "what-you-see-is-what-you-get" (WYSIWYG), ce qui permet un gain de temps et d'efficacité. 
Le programme Python et le fichier Qt designer sont consultables [ici](https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/tree/main/Interface%20Python).

<p align="center"><img width="457" alt="image" src="https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/assets/124165435/92f333f9-cdeb-42c1-bef6-6a3f9498cc0c">
 
Il est à noter que pour gérer à la fois la réception de données en continu et l’affichage du graphique déroulant, nous avons mis en place un thread dans notre programme Python. Le multithreading permet à un système d'exploitation la mise en place de plusieurs tâches qui fonctionnent en même temps.


## 8. Tests et résultats <a id="HuitiemeSection"></a>

Voici le setup d'utilisation du KTY2000.
<p align="center"><img width="400" alt="image" src="https://user-images.githubusercontent.com/124166161/235499366-d5575645-165a-4a30-af12-c5741c56be6b.png">

### 8.1 Banc de test <a id="HuitiemeSection1"></a>
 
Pour caractériser notre capteur, nous relevons la variation (relative ou non) de résistance de notre capteur en fonction de l'angle de flexion et de la déformation du capteur. Nous avons construit un banc de test avec l'aide de disques de papier cartonné de différents rayons de courbure, visibles ci-dessous. Les mesures ont été réalisées pour une déformation en traction et en compression, le tout en utilisant des crayons graphite de différentes duretés : 2B, HB et 2H.
<p align="center"><img width="250" alt="image" src="https://user-images.githubusercontent.com/124166161/235498021-97354d74-e4f6-4dfd-b12c-69112cfb68dd.png">
 
### 8.2 Résultats obtenus et analyses <a id="HuitiemeSection2"></a>
Les résultats de mesure sont consultables [ici](https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/blob/main/Datasheet/Relev%C3%A9%20de%20mesures.xlsx).

Les deux graphes suivant représentent la variation de la résistance relative (en %) en fonction de la déformation appliquée - compression et traction.
<p align="center"><img width="649" alt="image" src="https://user-images.githubusercontent.com/124165435/235679810-8c07bf9b-abfc-42d7-b863-36cdf839b4a3.png">
<p align="center"><img width="649" alt="image" src="https://user-images.githubusercontent.com/124165435/235679986-d3eed696-fc22-417e-b762-bcdb572f7c95.png">
 
Les mines les plus tendres contiennent une proportion plus élevée de particules de graphite. C’est donc pour cette raison que les traces de ce type de crayon paraissent plus foncées sur le papier. À l’inverse, les mines les plus dures contiennent beaucoup de liants argileux et apparaissent plus claires. Cela explique également que les résistances de mines de crayon les plus tendres sont plus faibles que les mines de crayon les plus dures. En effet, sous la traction, les particules de graphite sont davantage écartées les unes des autres favorisant la déconnexion des voies de conduction : le courant est donc minime, la résistance quant à elle augmente.  Sous compression, les particules de graphite contenues dans la trace de crayon se rapprochent, facilitant la conduction du courant à travers le réseau de percolation : la résistance s’abaisse naturellement.

Cette caractéristique est illustrée à travers la variation relative de résistance en fonction de la déformation du capteur. En effet, un crayon qui contient moins de particules de graphite comme le 2H dépose naturellement moins de graphite sur le substrat. Les variations de résistance sont donc plus significatives comme beaucoup de chemins de percolations sont créés ou rompus contrairement au 2B où les déformations n’induisent que de faibles variations relatives de résistance.
 
Il est également notable que le comportement en compression du flex-sensor se rapproche de celui du KTY2000. Nous pouvons en conclure que notre capteur graphite présente des similarités de fonctionnnement qu'un capteur industriel. **Cela confirme l'idée que le low-tech est une alternative pertinente pour le futur de l'industrie.**

### 8.3 Regard critique sur les résultats <a id="HuitiemeSection3"></a>
 
Il est important de souligner la variabilité des conditions expérimentales. Entre chaque relevé de points et malgré le fait que les pinces crocodiles sans dents étaient bien fixées, il se peut que l’attache du capteur ait bougée. Les résultats sont imprécis et pour certains discutables au vu de la qualité du montage mais suivent tout de même les lois physiques. 

Nous pourrions amener plusieurs pistes d'améliorations à notre projet :

- Améliorer notre banc de test afin de garantir des résultats optimaux mais surtout pour augmenter sa durée de vie et sa résistance. Par exemple, nous pourrions concevoir de le fabriquer par l'intermédiaire d'une imprimante 3D. 

- Améliorer notre PCB en y ajoutant un potentiomètre digital à la place de R2 afin de travailler sur une plus grande gamme de résistance. La tension de sortie serait ainsi modulée en fonction de la valeur de la résistance variable. 

- Améliorer le setup expérimental en commençant par l'ergonomie de notre PCB afin de le rendre plus fonctionnel pour la réalisation des mesures de résistance. Penser à un meilleur emplacement pour les différents composants, à un système d'accroche pour l'écran OLED, mais aussi pour les pinces crocodile dans le but de limiter le plus possible la variabilité des conditions expérimentales. 

 
## 9. Datasheet <a id="NeuvièmeSection"></a>
 
La datasheet du KTY2000 est consultable [ici](https://github.com/MOSH-Insa-Toulouse/2022-2023-4gp-almeras-lisoir/blob/main/Datasheet/Datasheet%20KTY2000.pdf). Elle reprend tous les concepts physiques ainsi que les résultats de mesures et leur analyse. D'autres courbes illustrant la variation de résistance en fonction de l'angle de flexion y figurent, venant compléter les affirmations énoncées tout au long de ce rendu. 
