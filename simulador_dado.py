'''
 Crea un simulador de dados
Simula el lanzamiento de un dado de 6 caras. El usuario
podrá lanzar el dado tantas veces como quiera y el 
programa debe mostrar el número obtenido.
'''
import random

def lanzar_dado():
    return random.randint(1,6)

while True:
    input("PRESIONA ENTER PARA LANZAR EL DADO")
    resultado= lanzar_dado()
    print(f"El dado ha caído en : {resultado}")
    continuar= input("¿QUIERES LANZAR OTRA VEZ (s/n): ").lower()
    if continuar != 's':
        break


