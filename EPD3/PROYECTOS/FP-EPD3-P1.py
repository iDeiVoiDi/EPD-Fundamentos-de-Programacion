print("\n|| Contador de Pasos ||\n")

# === VARIABLES ===
# Marcamos las constantes del programa
DIAS = 7
OBJETIVO = 10000

# Marcamos variables de estado
obj_posible = False

# Marcamos las variables
pasos = [0] * DIAS
total = 0

# === DATOS ===
# Preguntamos los datos necesarios
for i in range(DIAS):
    pasos[i] = (int(input(f"• ¿Cuantos pasos diste el dia {i + 1}?: ")))

# === LOGICA ===
# Pasos totales
for i in pasos:
    total += i

# Media
media = total // DIAS

# Supera OBJETIVO de pasos
for i in range(len(pasos)):
    if pasos[i] >= OBJETIVO:
        obj_cumplido = i + 1
        obj_posible = True


# === SALIDA ===
print("| Analizando datos...")
print(f"| El total de pasos es de: {total} pasos")
print(f"| La media de pasos es de: {media} pasos")
if obj_posible:
    print(f"| El objetivo fue cumplido por ultima vez el dia {obj_cumplido}")
else:
    print("| El objetivo no fue cumplido")