"""
Created on Thu Apr 13 18:02:26 2023

@author: ninaa
"""
import sys
import serial
import serial.tools.list_ports # pour la communication avec le port série
import matplotlib.pyplot as plt  # pour le tracé de graphe
from matplotlib import animation # pour la figure animée
import time
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from random import randint


qtCreatorFile = "Application Arduino.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#Fonction servant à convertir la résistance d'un capteur en son angle de flexion
def translate(value, fromMin, fromMax, from0, toMin, toMax,to0):

    
    if value <from0 and value>fromMin :
              
        if (from0 - fromMin) != 0 :
        
            valueScaled = float(value - fromMin) / float(from0-fromMin)
        
            return toMin + (valueScaled * (to0-toMin))
        
    if value <fromMax and value>from0 :
                
          if (fromMax - from0) != 0 :
          
              valueScaled = float(value - from0) / float(fromMax - from0)
          
              return to0 + (valueScaled * (toMax-to0))

#Fonction calculant le changement relatif en pourcentage de la résistance du capteur graphite par rapport à sa résistance R0
def variation_relative(R0, Rmes):
    if R0!=0:
        return abs((R0-Rmes)/R0)*100
    else:
        pass
          
        
    

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    
    port = QtCore.pyqtSignal(object) #Signal émis par la classe Window et reçu dans la class ThreadWorker
    
    def __init__(self):
        
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.pushButton_connect.clicked.connect(self.recup_port_arduino) #Connect a function to a clicked element on the GUI          
        self.pushButton_calibration.clicked.connect(self.donnees_calibration)
        self.pushButton_quit.clicked.connect(self.quit)
        
        #Initialisation des axes pour les deux graphiques
        self.X1 = list(range(100))
        self.X2 = list(range(100))
        
        self.Y1 = [] #Liste vide       
        self.Y2 = []
             
        
        #Titres des axes des deux graphiques
        self.graph_resistance_capteur.setLabel(axis='left', text='Résistance (MOhms)')
        self.graph_resistance_capteur.setLabel(axis='bottom', text='Temps (s)')
              
        self.graph_resistance_flexsensor.setLabel(axis='left', text='Résistance (Ohms)')
        self.graph_resistance_flexsensor.setLabel(axis='bottom', text='Temps (s)')

                    
   #Récupération des données nécessaires à la calibration des deux capteurs à l'aide d'un bouton sur l'IGU
    def donnees_calibration(self):
         self.R0_graphite = self.spinBox_R0_graphite.value()
         self.Rmax_graphite = self.spinBox_Rmax_graphite.value()
         self.Rmin_graphite = self.spinBox_Rmin_graphite.value()
         
        
        
    #Calcul et affichage de la valeur de l'angle du capteur en fonction de la résistance pour chaque capteur   
    def calibrate(self,data):
        try:    
            self.angle_graphite = translate(data[0],  self.Rmin_graphite, self.Rmax_graphite, self.R0_graphite,-90, 90, 0)
            self.label_angle_graphite.setText(str(format(self.angle_graphite,'.2f')))
           
            R_relative=variation_relative(self.R0_graphite, data[0]) 
            if type(R_relative) != type(None) :
                R_relative=format(R_relative,'.2f') #Limiter le format du résultat à 2 digits après la virgule
                self.label_resistance_relative_graphite.setText(str(R_relative))
        except:
            pass
    
        
    #Fonction qui connecte automatiquement l'ordinateur au port utilisé par la carte Arduino 
    def recup_port_arduino(self):
    
         ports = list(serial.tools.list_ports.comports())
    
         for p in ports:
             if 'Arduino' in p.description or 'USB-SERIAL CH340' in p.description :
                 try : 
                         self.mData = serial.Serial(port=p.device, baudrate=9600, bytesize=8, timeout=0.5, stopbits=1) #Open and configure the port
                         self.label_port_com.setText(self.mData.name)
                         QMessageBox.information(self, 'Succès','Connection au port réussie')
                         self.proofreading()
                         return self.mData 
                     
                 except serial.SerialException :
                        QMessageBox.information(self, 'Erreur','Problème de port')
      
                    
              
    def proofreading (self):
                    
        #Intialisation du thread       
        self.worker = ThreadWorker(self.port) #Création d'un thread instance thread depuis la classe ThreadWorker
        self.worker.start()
        self.port.emit(self.mData) #Création d'un signal émis et lu dans le thread.Ici, on envoie le statut port retourné par la fonction ci-dessus.       
        self.worker.data.connect(self.actual_values)
        self.worker.data.connect(self.calibrate)
        
        #Graph1 pour le capteur graphite
        pen1=pg.mkPen(color=(255, 0, 0)) #Coulur de la courbe
        self.data_line1 = self.graph_resistance_capteur.plot(self.Y1, pen=pen1) #Initialisation du graphe. Le graphe est vide au départ.
        self.worker.data.connect(self.plot1) #Trace le signal 'data' émis par le thread.
       

        #Graph2 pour le flexsensor    
        pen2=pg.mkPen(color=(0, 0, 255))
        self.data_line2 = self.graph_resistance_flexsensor.plot(self.Y2, pen=pen2) 
        self.worker.data.connect(self.plot2)
   
    #Affichage de la valeur réelle des résistances envoyées par l'Arduino et également visible sur l'écran OLED
    def actual_values(self, vals):
        if vals != []:
            self.label_resistance_graphite.setText(str(format(vals[0],'.2f')))       
            self.label_resistance_flex.setText(str(format(vals[1],'.2f')))
            self.label_angle_flex.setText(str(format(vals[2],'.2f')))
            
            
        
     
    #Tracé de l'évolution de la résistance du capteur graphite
    def plot1(self,data):
            
        self.X1 = self.X1[1:] 
        self.X1.append(self.X1[-1] + 1) 
                
        try :
            self.Y1 = self.Y1[-10:]
            self.Y1.append(float(data[0])) # Ajoute la dernière valeur lue à la liste 'data' 
            self.data_line1.setData(self.Y1) #Actualisation du plot
        except :
            pass
        
        
    #Tracé de l'évolution de la résistance du flex sensor
    def plot2(self,data): 
    
        self.X2 = self.X2[1:]  
        self.X2.append(self.X2[-1] + 1)  
      
        try :
            self.Y2 = self.Y2[-10:]
            self.Y2.append(float(data[1]))
            self.data_line2.setData(self.Y2) 
        except :
            pass
    
    
    #Gestion de l'arrêt du thread et du programme
    def quit(self): 
        self.worker.requestInterruption()           
        QtCore.QCoreApplication.instance().quit()
        QtWidgets.QMainWindow.close(self) 
        
            
class ThreadWorker(QThread):
    
    data = pyqtSignal(list) #Signal émis par la classe ThreadWorker et reçu dans la class Main

    def __init__(self, rs):
        super(ThreadWorker, self).__init__()
        rs.connect(self.port_connection)

    @QtCore.pyqtSlot(object)  
    def port_connection(self, val):
        self.rs = val
            
    def run(self):
        
        self.list = []

        while True:
            time.sleep(0.5)
            self.list.clear() #Efface les valeurs précédentes stockées dans la liste
                               
            self.line = self.rs.readline()
            self.listeDonnees = self.line.strip().split() #Retire les caractères d'espacement en début et fin de chaîne et extrait les différentes données
            resistance_graphite = float(self.listeDonnees[0].decode())#Récupère le premier élément de la liste
            resistance_flex = float(self.listeDonnees[1].decode())
            angle_flex = float(self.listeDonnees[2].decode())
            
            #Traite le cas où le cpateur envoie une donnée erronnée
            if str(resistance_graphite) != 'inf' and str(resistance_flex) != 'inf' and str(resistance_flex) != 'inf' :
                self.list.append(resistance_graphite) #Append the received value to the list
                self.list.append(resistance_flex)
                self.list.append(angle_flex)
            
            self.data.emit(self.list)
            
            if self.isInterruptionRequested(): #Interruption demandée dans la Main Window
                self.rs.close() #Fermeture du port série
                break

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())