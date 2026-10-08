alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]
aprobados = 0
suspensos = 0
sumaNotaMedia = 0
for alumno in alumnos:
    nombre = alumno["nombre"]
    nota = alumno["nota"]
    estaAprobado = ""
    sumaNotaMedia += nota
    if nota < 5:
        estaAprobado = "SUSPENDIDO"
        suspensos +=1
    else:
        estaAprobado = "APROBADO"
        aprobados +=1
    
    print(f"Alumno: {nombre.upper()}, Nota: {alumno["nota"]}, {estaAprobado} ")
notaMedia = sumaNotaMedia / len(alumnos)
print(f"Hay {aprobados} alumnos Aprobados y hay {suspensos} suspendidos")
print(f"La nota media es {notaMedia}")
