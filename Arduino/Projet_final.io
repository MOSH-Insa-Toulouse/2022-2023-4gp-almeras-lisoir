#include <SoftwareSerial.h>
#define baudrate 9600
#include <Adafruit_SSD1306.h>

const float VCC = 5;      // Tension de 5V délivrée par l'arduino

/*FLEXXXXX*/

#define flexPin A1    // Pin connected to voltage divider output
const float R_DIV = 47000.0;  // resistor used to create a voltage divider
const float flatResistance = 21100.0; // resistance when flat
const float bendResistance = 10000.0;  // resistance at 90 deg

/*OLED*/

//Capteur graphite
#define mesPin A0
float mes ;
float final_resistance ; 

// constantes liées à l'écran OLED
#define nombreDePixelsEnLargeur 128         // Taille de l'écran OLED, en pixel, au niveau de sa largeur
#define nombreDePixelsEnHauteur 64          // Taille de l'écran OLED, en pixel, au niveau de sa hauteur
#define brocheResetOLED         -1          // Reset de l'OLED partagé avec l'Arduino (d'où la valeur à -1, et non un numéro de pin)
#define adresseEcranOLED     0x3C           // Adresse de "mon" écran OLED sur le bus i2c (généralement égal à 0x3C ou 0x3D)
Adafruit_SSD1306 ecranOLED(nombreDePixelsEnLargeur, nombreDePixelsEnHauteur, &Wire, brocheResetOLED);


/*Définition des valeurs de résistance du circuit qui seront uniquement utilisées pour le calcul de conversion TENSION(V) EN RESISTANCE(OHM)*/

float R1 = 100000.0 ;
float R2 = 1000.0 ;
float R3 = 100000.0 ;
float R5 = 10000.0 ;

void setup() {
  
  /*FLEXXXXX*/
  
  Serial.begin(baudrate);
  pinMode(flexPin, INPUT);

  /*OLED*/
  
  if(!ecranOLED.begin(SSD1306_SWITCHCAPVCC, adresseEcranOLED))
    while(1);                               // Arrêt du programme (boucle infinie) si échec d'initialisation
   
}

void loop() {

  //Qui pourra etre visible dans le moniteur serie//

  /*FLEXXXXX*/
  
  // Lecture de A1, calcul de la tension puis de la résistance du flex sensor
  int ADCflex = analogRead(flexPin);
  float Vflex = ADCflex * VCC / 1023.0;
  float Rflex = R_DIV * (VCC / Vflex - 1.0);
  //Serial.println("Resistance du flexsensor: " + String(Rflex) + " Ohms");
  //Serial.println();

  // Use the calculated resistance to estimate the sensor's bend angle:
  float angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  //Serial.println("Angle du flexsensor: " + String(angle) + " degrés");
  //Serial.println();

/*CAPTEUR GRAPHITE*/

  //Serial.println("Résistance du capteur: " + String(final_resistance) + " MOhm");
  //Serial.println();

  Serial.println(String(final_resistance) + " " + String(Rflex) + " " + String(angle));
  
  /*OLED*/
  
   //Capteur graphite
   
    mes = analogRead(mesPin);
    mes=(mes*5.0)/1024.0 ;
    final_resistance = ((VCC/mes)*(R1/R2)*(R2+R3)-(R5+R1))* 0.000001 ; //conversion TENSION(V) EN RESISTANCE(OHM) + *10^-6 pour avoir la résistance de notre capteur en MOhm.
   
    boolean bCouleurInverse = false;
    ecranOLED.clearDisplay();                                   // Effaçage de l'intégralité du buffer
    ecranOLED.setTextSize(1);                                   // Taille des caractères (1:1)
    ecranOLED.setCursor(0,0);                                   // Déplacement du curseur en position (0,0), c'est à dire dans l'angle supérieur gauche

   if(bCouleurInverse)
       ecranOLED.setTextColor(SSD1306_BLACK, SSD1306_WHITE);   // Couleur du texte, et couleur du fond
    else
       ecranOLED.setTextColor(SSD1306_WHITE); 


    ecranOLED.print("Res capteur: ");
    ecranOLED.println();
    ecranOLED.println();
    ecranOLED.print(String(final_resistance) + " MOhm");
    ecranOLED.println();
    ecranOLED.println();
    ecranOLED.println();
    ecranOLED.println("Res flexsensor: ");
    ecranOLED.println();
    ecranOLED.print(String(Rflex) + " Ohms");

    bCouleurInverse =! bCouleurInverse;
    ecranOLED.display();                            // Transfert le buffer à l'écran
  
delay(500);
  }
