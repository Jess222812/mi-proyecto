# Sistema de calificaciones utilizando arreglos o vectores

# Arreglo con las calificaciones de 5 estudiantes
calificaciones = [85, 67, 92, 74, 58]

print("===== SISTEMA DE CALIFICACIONES =====")

# 1. Mostrar todas las calificaciones
print("\nCalificaciones iniciales:")
for i in range(len(calificaciones)):
    print("Estudiante", i + 1, ":", calificaciones[i])

# 2. Acceder a un elemento mediante su indice
print("\nCalificacion del estudiante 3:", calificaciones[2])

# 3. Modificar una calificacion
calificaciones[4] = 80
print("\nSe modifico la calificacion del estudiante 5.")

# 4. Recorrer el arreglo y aplicar una condicion
suma = 0
aprobados = 0
reprobados = 0

for nota in calificaciones:
    suma += nota

    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

# 5. Calcular el promedio
promedio = suma / len(calificaciones)

# 6. Buscar la calificacion mas alta y mas baja
mayor = max(calificaciones)
menor = min(calificaciones)

# 7. Mostrar los resultados
print("\n===== RESULTADOS =====")
print("Calificaciones actualizadas:", calificaciones)
print("Promedio general:", round(promedio, 2))
print("Calificacion mas alta:", mayor)
print("Calificacion mas baja:", menor)
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)

print("\n===== FIN DEL PROGRAMA =====")
