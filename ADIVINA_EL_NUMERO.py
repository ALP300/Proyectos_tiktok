'''
ADIVINA EL NÚMERO
'''
import random

def adivinanza():
    numero= random.randint(1,100)
    intentos=0
    
    while True:
        intento_usuario= int(input("Adivina el número entre 1 y 100:  "))
        intentos+=1
        if intento_usuario < numero:
            print("El número es mayor")
        
        elif intento_usuario > numero:
            print("El número es menor")
        
        else:
            print(f"¡FELICIDADES! Has adivinado el número en {intentos} intentos")
            break

adivinanza()
    
    