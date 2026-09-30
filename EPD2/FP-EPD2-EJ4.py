print("| Sugerencia de amistad |\n")

# Marco las variables de estado
actividad_interior = False

# Recolección de los datos del usuario
temperatura = float(input("• ¿Que temperatura hay en el exterior?: "))
clima = input("• ¿Hay lluvia en este momento?: (si/no) ")

# Lógica del programa
if clima == "si":
    actividad_interior = True
elif temperatura < 15 or temperatura > 25:
    actividad_interior = True

# Muestra de los datos obtenidos
print("| Análisis de la ubicación...")
if actividad_interior:
    print("→ RECOMENDADO EN INTERIOR")
else:
    print("→ RECOMENDADO EN EXTERIOR")
