'''
LISTA DE REGALOS
PARA NAVIDAD
'''
def gestionar_regalos():
    regalos={}
    while True:
        print("\n1. AGREGAR REGALO DE NAVIDAD")
        print("2. VER LISTA DE REGALOS DE NAVIDAD")
        print("3. ELIMINAR REGALO")
        print("4. SALIR")
        opcion= input("Elige una opción: ")
        
        if opcion=="1":
            regalo= input("Ingresa el nombre del regalo: ")
            cantidad= int(input(f"¿Cuántos {regalo} quieres: "))
            regalos[regalo]= regalos.get(regalo,0)+cantidad
        elif opcion=="2":
            print("\nLISTA DE REGALOS")
            for regalo, cantidad in regalos.items():
                print(f"{regalo}: {cantidad}")
            
        elif opcion=="3":
            regalo= input("Ingresa el nombre del regalo: ")
            if regalo in regalos:
                del regalos[regalo]
                print(f"El regalo {regalo} ha sido eliminada")
            else:
                print(f"El regalo {regalo} no se encuentra en el diccionario")
            
        elif opcion=="4":
            break
        
        else:
            print("OPCIÓN INVÁLIDA")
                
            
gestionar_regalos()
 