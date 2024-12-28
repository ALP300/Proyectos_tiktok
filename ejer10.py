'''
JUEGO DE PIEDRA PAPEL O TIJERA
'''
import random

opciones= ["piedra", "papel","tijera"]
print("¡BIENVENIDO AL JUEGO DE PIEDRA PAPEL O TIJERA!")
jugador_puntaje=0
computador_puntaje=0

while True:
    jugador= input("Elige piedra, papel o tijera (o escribe 'salir' para terminar): ").lower()
    if jugador=="salir":
        break
    if jugador not in opciones:
        print("Opción inválida, ingresa nuevamente")
        continue

    computadora= random.choice(opciones)
    print(f"La computadora eligió {computadora}")
    
    if jugador == computadora:
        print("Es Empate")
    
    elif (jugador=="piedra" and computadora=="tijera") or \
         (jugador=="papel" and computadora=="piedra") or \
         (jugador=="tijera" and computadora=="papel"):
        
        print("Ganaste!!!!!!!!!!")
        jugador_puntaje+=1
    
    else:
        print("Perdiste!!!")
        computador_puntaje+=1
             
    print(f"Puntaje: Tú: {jugador_puntaje} - Computadora: {computador_puntaje}")

print("Gracias por jugar")
        
        