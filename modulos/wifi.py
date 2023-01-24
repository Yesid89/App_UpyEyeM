import network, time
from machine import Pin

red = "" #Nombre Red
password = "" #Clave Red 

#Funcion para conectar wifi
def conectaWifi ():
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      if miRed.isconnected(): 
          #print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig()) 
          return True
      else:
          print ("Red no activada")
          miRed.active (False)



