'''
Juego de la ruleta
Crea un juego de ruleta en el que el usuario tenga que 
elegir un número entre 0 y 36, y luego la computadora 
"gira" la ruleta y elige un número aleatorio.

 numero_usuario= int(input("Elige un número de 0 al 36: "))
    numero_ruleta= random.randint(0,36)
    print(f"La ruleta ha caído en: {numero_ruleta}")
'''
import random

def juego_ruleta():
    while True:
        try:
            numero_usuario= int(input("Elige un número de 0 al 8: "))
            if 0<= numero_usuario<=8:
                break
            else:
                print("Por favor, elige un número del 0 al 36")
        except ValueError:
            print("Por favor, ingresa un número válido")
            
            
    numero_ruleta= random.randint(0,8)
    print(f"La ruleta ha caído en: {numero_ruleta}")
    
    if numero_usuario== numero_ruleta:
        print("GANASTE, LE ATINASTE")
    else:
        print("INTENTA NUEVAMENTE!")
    
juego_ruleta()    
   
