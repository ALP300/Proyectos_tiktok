'''
Crea un contador regresivo para una 
cuenta atrás
Haz un contador regresivo que diga "
¡Feliz Navidad!" cuando llegue a cero, 
pero que también imprima "¡Casi!" cuando
falta menos de 5 segundos.
'''
import time

def cuenta_regresiva(segundos):
    while segundos>0:
        if segundos<5:
            print(("¡CASI!"))
        else:
            print(f"{segundos} segundos restantes para Navidad")
        
        time.sleep(1)
        segundos-=1
    print("¡Feliz navidad!")
    
segundos = int(input("¿CUÁNTOS SEGUNDOS PARA LA CUENTA REGRESIVA?: "))
cuenta_regresiva(segundos)