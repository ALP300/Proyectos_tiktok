'''
¿Cómo puedes guardar los objetivos 
de Año Nuevo, organizados por mes, 
en un archivo de texto y luego 
mostrarlos en la consola?
'''

def guardar_objetivos(objetivos):
    with open("Objetivos_2025.txt","w",encoding="utf-8") as archivo:
        archivo.write("🎯 Objetivos de Fin de Año 🎯")
        archivo.write("="*20+"\n")
        for mes, objetivo in objetivos.items():
            archivo.write(f"{mes}: {objetivo}\n")
        
    print("Objetivos guardados de manera exitosa!")

def main():
    meses=["Enero", "Febrero","Marzo","Abril", "Mayo", "Junio",
    "Julio", "Agosto" ,"Septiembre","Octubre", "Noviembre", "Diciembre"]
    
    objetivos = {}
    print("Bienvenido a tu gestor de objetivos del año!!!!!")
    for mes in meses:
        objetivo=input(f"Por favor ingresa el objetivo de {mes}: ")
        objetivos[mes]= objetivo

    print("\nRESUMEN DE OBJETIVOS: ")
    for mes, objetivo in objetivos.items():
          print(f"{mes}:{objetivo}")
    
    guardar_objetivos(objetivos)

if __name__== "__main__":
    main()