print("\n|| Analisis de los Partidos ||\n")

# === VARIABLES ===
# Marco las constantes del programa
PARTIDOS = 8
OBJETIVO = 100

# Marcamos las variables
puntos = [0] * PARTIDOS
total = 0
partidos_obj = 0
mejor = 0
peor = 0

# === DATOS ===
for i in range(PARTIDOS):
    puntos[i] = int(input(f"• ¿Cual fue la puntuacion del partido {i + 1}?: "))

# === LOGICA ===
for i in puntos:
    total += i # Calculo puntos totales

    if i >= OBJETIVO: # Calculo de partidos q superan el OBJETIVO de puntos
        partidos_obj += 1

    if peor == 0: # Pongo un valor inicial
        peor = i 
    if i >= mejor: # Busqueda del mejor y peor partido
        mejor = i
    if i <= peor:
        peor = i

# Media
media = round(total / PARTIDOS, 2)

# === SALIDA ===
print("| Analizando datos...")
print(f"| La puntuacion total es de: {total} puntos")
print(f"| La media de los puntos es de: {media} puntos")
print(f"| Los partidos que superaron {OBJETIVO} puntos es de: {partidos_obj} partidos")
print(f"| La mejor puntuacion es de: {mejor} puntos, mientras que la peor es de: {peor} puntos")
