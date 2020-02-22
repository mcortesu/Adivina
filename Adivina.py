'''
Aplicación que implementa el juego de Adivina, consistente ne adivinar un número que se encuentra entre
un mínimo y un máximo.
La aplicación guarda y lle los resultados en un fichero llamado resultados.txt.
La información almacenada es una lista de diccionarios, estando compuesto cada diccionario por:
- el nombre del jugador
- el record
- una lista con los intentos fallados
- la fucha y hora de la partida

En esta versión se supone que cada jugador es distinto, es decir a jugadores con mismo nombre los considera distintos.

'''

import random
import datetime
from funciones import leerResultados, ordenaLista, imprimePrimeros, jugarPartida, escribeFichero

minimo = 1
maximo = 100
nom_fichero ="resultados.txt"
n_records = 3  # Nº de marcadores a mostrar
#secreto = random.randint(minimo, maximo)

print("Bienvenido al juego de ADIVINA")

while True:
    nombre = input("Escriba s nombre: ")
    # print("Bienvenido %s:", {nombre})
    print("   1 - Mostrar marcadores.")
    print("   2 - Jugar partida facil.")
    print("   3 - Jugar partida difícil.")
    print("   4 - Salir.")
    opcion = input("   Elija una opción: ")

    if opcion == "1":
        marcadores = leerResultados(nom_fichero)  # Obtengo una lista con todos los resultados
        marcadores = ordenaLista(marcadores)

        print("Los {} primeros puestos son: ".format(n_records))
        imprimePrimeros(marcadores, n_records)
    elif opcion == "2" or opcion == "3":
        partida = {"nombre": nombre}
        partida.update(jugarPartida(int(opcion)-2, minimo, maximo))
        partida.update({"fecha": str(datetime.datetime.now())})
        escribeFichero(nom_fichero, partida)
    elif opcion == "4":
        print("Gracias por jugar. Hasta otra.")
        break
    else:
        print("ERROR: Opción incorrecta.")



