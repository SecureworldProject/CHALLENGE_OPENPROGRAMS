from math import log10, sqrt

import os
from pathlib import Path
import time
#para instalar el modulo easygui simplemente:
#pip3 install easygui
# o bien py -m pip install easygui
import easygui 
#import lock

#pip3 install psutil
#o bien py -m pip install psutil
import psutil

#import socket
#import fnmatch
# variables globales
# ------------------
props_dict={} 
DEBUG_MODE=True

def init(props):
    global props_dict
    print("Python: Enter in init")
    
    #props es un diccionario
    props_dict= props

    return 0


def executeChallenge():
    print("Starting execute")
        
    #mecanismo de lock BEGIN, para garantizar una sola interaccion con user a la vez
    #-----------------------
    #no lo necesito porque no es intrusivo
    #lock.lockIN("hostname")
    
    #obtenemos lista real
    lista_progs=[]
    for i in psutil.process_iter():
        lista_progs.append(i.name())
    # no vamos a imprimir la lista porque es enorme
    lista= props_dict["process_list"]

    cad=""
    for i in lista:
        if i in lista_progs:
            cad=cad+"1"
            continue
        else:
            cad=cad +"0"
    print ("cad:",cad)
    #print ("lista_programs:" , lista_progs)

    
    #mecanismo lock out. no lo usamos porque no es necesario en este challenge (no es intrusivo)
    #lock.lockOUT("hostname")
    
    #ahora extraemos la parte del hostname comun a los PC corporativos
    #lenstart=props_dict["hostname_len"]
    #print ("your hostname=", hostname)
    #cad= hostname[:lenstart]
    #print ("subkey is ", cad)
    #cad="hola"
    
    key = bytes(cad,'utf-8')
    key_size = len(key)

    result =(key, key_size)
    print ("result:",result)
    return result



if __name__ == "__main__":
    # la lista de programas se puede cambiar:
    # chrome, notepad, teams ,
    # antivirus symantec "ccSvcHst.exe"
    # antivirus IPS utilities "sisipsutil.exe"
    # cisco user interface "vpnui.exe"
    # lenovo power management service "ibmpmsvc.exe"
    
    midict={"process_list": ("chrome.exe","notepad.exe", "Teams.exe", \
                      "ccSvcHst.exe", "sisipsutil.exe","vpnui.exe", \
                      "ibmpmsvc.exe")} 
    init(midict)
    executeChallenge()

