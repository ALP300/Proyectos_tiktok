'''
Escribir un programa que almacene las asignaturas 
de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte 
al usuario la nota que ha sacado en cada asignatura 
y elimine de la lista las asignaturas aprobadas. Al 
final el programa debe mostrar por pantalla 
las asignaturas que el usuario tiene que repetir.
'''
materias=["Física","Historia","Trigonometria","Geometría","Tutoria"]
aprobados=[]

for materia in materias:
    nota= float(input(f"¿Qué nota has sacado {materia}?: "))
    if nota>=10:
        aprobados.append(materia)

for aprobado in aprobados:
    materias.remove(aprobado)

print("Tienes que repetir: "+str(materias))