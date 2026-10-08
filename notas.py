alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]
def calcular_media(lista):
    sumaNota = 0
    for x in lista:
       sumaNota += x["nota"]

    if len(lista) == 0:
        return 0
    else:
        return sumaNota/len(lista)
aprobados = 0
suspensos = 0
for alumno in alumnos:
    nombre = alumno["nombre"]
    nota = alumno["nota"]
    estaAprobado = ""
    if nota < 5:
        estaAprobado = "SUSPENDIDO"
        suspensos +=1
    else:
        estaAprobado = "APROBADO"
        aprobados +=1
    
    print(f"Alumno: {nombre.upper()}, Nota: {alumno["nota"]}, {estaAprobado} ")
notaMedia = calcular_media(alumnos)
print(f"Hay {aprobados} alumnos Aprobados y hay {suspensos} suspendidos")
print(f"La nota media es {notaMedia}")
