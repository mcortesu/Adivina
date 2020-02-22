"""
Este fichero contiene funciones para simplificar el contenido de la aplicación Adivina

El fichero que almacena los resultados debe contener una lista con los resultados de los distintos jugadores.
Los resultados son un diccionario con la siguiente información:
nombre: nombre del jugador
intentos: el número de intentos para adivinar el número
jugadas: una lista con cada jugada, los nº fallados y el último el nº secreto
fecha: fecha en la que se jugó
"""

import json
import random
import os
from operator import itemgetter


"""
Mediante la función abrirFichero, si existe el fichero nom_fich lo abre 
(se supone que el fichero tiene los datos en formato correcto) y 
lo devuelve, si no existe lo crea y escribe [] 
(de lo contrario daría error la función json.loads)
 y posteriormente lo devuelve.
"""
def abrirFichero(nom_fich):
    try:
        fichero = open(nom_fich,"r")
    except FileNotFoundError:
        fichero = open(nom_fich, "w")
        #fichero.write("[]")
        fichero.close()
        fichero = open(nom_fich, "r")
    finally:
        return fichero



'''
Con la función leerResultados se leen los resultados de un fichero.
Hay que considerar que los resultados están correctamente introducidos en el fichero
Cada línea del fichero es una partida
Se devuelve una lista

'''
def leerResultados(nom_fich):
    fichero = abrirFichero(nom_fich)
    marcadores = []
    path = os.path.abspath(nom_fich)        # Obtiene la ruta absoluta.
    if os.path.getsize(path) > 0:  # El fichero tiene contenido??
        for line in fichero:
            marcadores.append(json.loads(line))
            # marcadores.append(line) --> daría como resultado una lista de string --> ['{"nombre": "marcos", "edad": 43}\n', '{"nombre": "luis", "edad": 12}\n', '{"nombre": "juan", "edad": 34}']
    fichero.close()
    return marcadores

'''
La función ordenaLista recibe una lista desordenada y la devuelve ordenada.
Cada elemento de la lista es un diccionario
Más información de esta ordenación en la documentación de Python --> Sorting HOW TO
'''
def ordenaLista(lista_desordenada):
    if lista_desordenada == []:
        return lista_desordenada
    else:
        return sorted(lista_desordenada, key=itemgetter("intentos"))

'''
Imprime los primeros marcadores
'''
def imprimePrimeros(lista, primeros):
    l_primeros = lista[:primeros]
    for marcador in l_primeros:
        print("Jugador: " + marcador["nombre"] + " - Intentos: " + str(marcador["intentos"]) + " - Fecha: " + marcador[
            "fecha"])


'''
Esta función recibe una cadena y devuelve True si es un entero y False si no lo es
'''
def isEntero(texto):
    try:
        int(texto)
        return True
    except:
        return False

"""
Comprueba que se introduce un Entero y que está entre los límites. Si no es así, indica ERROR
y vuelve a pedirlo.
"""
def numeroValido(texto, minimo, maximo):
    while True:
        if isEntero(texto) == False:
            texto = input("ERROR: Debe introducir un número. Vuelva a intentarlo: ")
        else:
            numero = int(texto)
            if numero < minimo or numero > maximo:
                texto = input("ERROR. El número debe estar entre %s y %d. Vuelva a intentarlo: " % (minimo, maximo))
            else:
                return numero


"""
Esta función almacena en el fichero los resultados de una partida, que es un diccionario
Cada partida se almacena en una línea

"""
def escribeFichero(nom_fichero, partida):
    with open(nom_fichero, "a") as fichero:
        fichero.write(json.dumps(partida) + "\n")   # para que añada una nueva línea se pone \n


"""
En esta función se introduce un nivel (o - fácil, 1 - dificil) y un intervalo y
pide adivinar un número entre esos valores.
Devuelve el resultado de la partida mediante un diccionario formado por el número de intentos
y la lista de los intentos. 
Nos podíamos ahorar el número de intentos, pues con los intentos se puede calcular.
"""
def jugarPartida(nivel, minimo, maximo):
    secreto = random.randint(minimo, maximo)
    contador = 1
    marcadores = []
    jugadas = []  # Se almacena una lista con los fallos

    while True:
        guess = input("Escribe un número entre {} y {}: " .format(minimo, maximo))
        guess = numeroValido(guess, minimo, maximo)  # Comprueba que se introduce un número entre los límites

        jugadas.append(guess)  # Se pone aquí para que el último elemento de la lista sea el número secreto

        if guess == secreto:
            print("BRAVO, lo has conseguido tras " + str(contador) + " intentos.")
            return {"intentos": contador, "jugadas": jugadas}
        else:
            if nivel == 0:  # Facil
                if guess < secreto:
                    print("El número secreto es mayor, vuelva a intentarlo.")
                else:
                    print("El número secreto es menor, vuelva a intentarlo.")
            elif nivel == 1:   # Dificil
                print("El número secreto no corresponde con el número introducido, vuelva a intentarlo.")

            contador += 1

#escribeFichero("resultados.txt", {"nombre": "manolo", "edad": 12})
#escribeFichero("resultados.txt", {"nombre": "pedro", "edad": 65})
#print(leerResultados("resultados.txt"))
#print(partida(0, 1, 50))

