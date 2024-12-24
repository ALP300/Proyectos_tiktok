'''
TARJETA NAVIDEÑA
'''
def crear_tarjeta():
    print("¡Bienvenido al generador de tarjetas de navidad! 🎅🎄")
    destinatario= input("¿Para quién es la tarjeta?: ")
    mensaje= input("Escribe tu mensaje navidad: ")
    remitente= input("¿Quién la tarjeta?: ")
    
    tarjeta= f"""
    ***************************
    *                         *
    *     🎄Feliz Navidad     *
    *                         *
    * *************************
    
    Para: {destinatario}
    
    {mensaje}
    
    Con mucho cariño, de:
    {remitente}
    
    ***************************
    
    """
    print("\n Tu tarjeta navideña: ")
    print(tarjeta)
    
    guardar= input("¿Quieres guardar la tarjeta como archivo(sí/no): ").lower()
    "ALDAIR EDUARDO"
    "ALDAIR_EDUARDO"
    if guardar=="sí":
        nombre_archivo= f"tarjeta_navidad_{destinatario.replace(' ','_')}.txt"
        with open(nombre_archivo,"w",encoding="utf-8") as archivo:
            archivo.write(tarjeta)
        print(f"Tu carrera ha sido guardada: '{nombre_archivo}'")
        
    else:
        print("Tarjeta no guardada!")
    
if __name__=="__main__":
    crear_tarjeta()