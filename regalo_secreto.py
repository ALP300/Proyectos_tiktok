'''
INTERCAMBIO DE REGALOS SECRETO
'''
import random

def intercambio_regalo(participantes):
    destinatarios= participantes[:]
    #[Leo, Jose, Abel, Davxdz]    
    #[Leo, Jose, Abel, Davxdz]
    #[Jose, Leo, Davxdz, Abel]
    random.shuffle(destinatarios)
    intercambio={}
    for i, participantes in enumerate(participantes):
        while destinatarios[i]== participantes:
            random.shuffle(destinatarios)
        intercambio[participantes]= destinatarios[i]
        
    return intercambio

if __name__== "__main__":
    print("INTERCAMBIO DE REGALOS")
    participantes= input("Introduce los participantes separados por coma: ").split(",")
    participantes=[p.strip() for p in participantes]
    
    if len(participantes)<2:
        print("Necesitas al menos 2 participantes")
    else:
        intercambio=intercambio_regalo(participantes)
        print("\nResultado del intercambio: ")
        for dador, receptor in intercambio.items():
            print(f"{dador}--->{receptor}")
    
    #Leo , pepe , nil , alan
    #['Leo','pepe','nil']