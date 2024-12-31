'''
Descripción del problema:

Un usuario quiere organizar sus metas de Año Nuevo de 
manera efectiva y enfocarse en las más importantes primero.
Necesita un programa que permita:

Ingresar varias metas.
Asignar una prioridad a cada meta (del 1 al 5, siendo 5 la más 
importante).
Ordenar automáticamente las metas según su prioridad y mostrar 
la lista final.
'''

def planificar_metas():
    print("Bienvenido al Planificador de Metas de Año Nuevo! ")
    metas=[]
    
    while True:
        meta=input("\nIngresa una meta (o escribe salir para terminar): ")
        if meta.lower()=="salir":
            break
        
        prioridad= int(input(f"¿Qué tan importante es la meta '{meta}'? (1= Baja Prioridad, 5= Alta prioridad): "))
        metas.append((meta,prioridad))
    
    print("\nTus metas ordenadas por prioridad: ")
    metas_ordenadas= sorted(metas, key= lambda x: x[1], reverse=True )
    for idx, (meta, prioridad) in enumerate(metas_ordenadas,1):
        print(f"{idx}. {meta} (Prioridad: {prioridad})")
    
    print("¡Buena suerte con tus metas!")
    
if __name__== "__main__":
    planificar_metas()