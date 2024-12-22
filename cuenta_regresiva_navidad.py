'''
CUENTA REGRESIVA PARA NAVIDAD
'''
from datetime import date

def dias_para_navidad():
    hoy= date.today()
    navidad= date(hoy.year,12,25)
    dias_faltantes= (navidad-hoy).days
    if dias_faltantes>0:
        print(f"Hoy es {hoy.strftime('%d de %B')}. Faltan {dias_faltantes}")
    elif dias_faltantes==0:
        print("¡¡¡¡FELIZ NAVIDAD!!!!")
    else:
        print("Ya pasó navidad, ¡FELIZ AÑO NUEVO!")
        
dias_para_navidad()