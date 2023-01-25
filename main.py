from sys import path
path.append('..\\modulos')

from machine import Pin
from utime import sleep
from modulos.hcsr04 import HCSR04
from modulos.wifi  import conectaWifi
import modulos.utelegramsendtext as telegram

ultrasonico = HCSR04(trigger_pin=12, echo_pin=13)
ConectarWifi = conectaWifi()

def main():    
    if ConectarWifi:
        print ("Conexión exitosa!")
        i = 1
        while True:
            distancia = ultrasonico.distance_cm()
            print("{:.0f}".format(distancia))
            sleep(1)
            if distancia < 50:
                telegram.bot_send_text("Hay alguien cerca, verificar cámara puerta")
                print("Alerta  distancia menor a 50 cm!!! sensor de proximidad en: ", distancia )
                sleep(50)
    else:
        print ("Imposible conectar")


if __name__==("__main__"):
    main()
