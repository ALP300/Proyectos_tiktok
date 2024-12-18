import random

emojis={
    ":)":"feliz",
    ":o":"asombro",
    ":v":"pacman",
    "T-T":"llorando",
    ">:(":"asao",
    "._.":"serio",
    ":3":"kawaii",
    ":(":"triste"
}

#FELIZ
emoji,sentimiento= random.choice(list(emojis.items()))

print("Bienvenido al juego de ¡ADIVINA EL EMOJI!")
print(f"Adivina el sentimiendo asosiado con este emoji: {emoji}")

while True:
    respuesta= input("¿Qué sentimiento crees que represente?: ").lower()
    if respuesta==sentimiento:
        print("CORRECTO :D")
        break
    else:
        print("INCORRECTO, PISTA: La letra empieza con '{}'".format(sentimiento[0]))


print("¡GRACIAS POR JUGAR!")
    