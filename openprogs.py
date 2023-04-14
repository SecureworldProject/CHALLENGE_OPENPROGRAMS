# To install psutil run any of the following commands:
#   > pip3 install psutil
#   > py -m pip install psutil
import psutil




# Variables globales
# ------------------
props_dict = {}
DEBUG_MODE = True



def init(props):
    global props_dict
    print("CHALLENGE_OPEN_PROGS --> Enter in init")

    #props es un diccionario
    props_dict = props

    return 0


def executeChallenge():
    print("CHALLENGE_OPEN_PROGS --> Starting execute")

    # Obtenemos lista de procesos abiertos actualmente
    lista_progs = []
    for i in psutil.process_iter():
        lista_progs.append(i.name())
    # No vamos a imprimir la lista porque es enorme
    #print("CHALLENGE_OPEN_PROGS --> List of currently open programs:" , lista_progs)

    # Limpiar la lista de programas a comprobar
    lista = props_dict["process_list"] # lista es un string con subcadenas separadas por ","
    lista = lista.replace(" ", "")
    lista = lista.split(",")
    print("CHALLENGE_OPEN_PROGS --> List of programs to check:", lista)

    # Generar la clave
    print("CHALLENGE_OPEN_PROGS --> Creating key...")
    cad = ""
    for i in lista:
        if i in lista_progs:
            cad = cad + "1"
            continue
        else:
            cad = cad + "0"
    print("CHALLENGE_OPEN_PROGS --> key:", cad)

    key = bytes(cad,'utf-8')
    key_size = len(key)

    result = (key, key_size)
    print("CHALLENGE_OPEN_PROGS --> result:", result)
    return result



if __name__ == "__main__":
    # La lista de programas se puede cambiar. Ejemplos:
    # chrome, notepad, teams ,
    # antivirus symantec "ccSvcHst.exe"
    # antivirus IPS utilities "sisipsutil.exe"
    # cisco user interface "vpnui.exe"
    # lenovo power management service "ibmpmsvc.exe"

    midict = {"process_list": ["chrome.exe","notepad.exe", "Teams.exe", \
                      "ccSvcHst.exe", "sisipsutil.exe","vpnui.exe", \
                      "ibmpmsvc.exe"]} 

    midict = {"process_list": "chrome.exe,notepad.exe, Teams.exe,ccSvcHst.exe,sisipsutil.exe,vpnui.exe,ibmpmsvc.exe",
            "module_python": "hola chavales"} 

    init(midict)
    executeChallenge()
