print("| Sugerencia de amistad |\n")

# Marco las variables de estado
misma_ciudad = False
posible_amistad = False

# Recolección de los datos del usuario
amigos_comun = int(input("• ¿Cuantos amigos en común posees con el usuario?: "))
coinciden_ciudad = input("• ¿Coinciden usted y el usuario en la misma ciudad?: (si/no) ")

# Lógica del programa
if coinciden_ciudad == "si":
    misma_ciudad = True

if amigos_comun > 10:
    posible_amistad = True
elif amigos_comun > 5 and misma_ciudad:
    posible_amistad = True

# Muestra de los datos obtenidos
print("| Análisis de la amistad...")
if posible_amistad:
    print("→ AMISTAD COMPATIBLE")
else:
    print("→ AMISTAD QUIZÁS NO COMPATIBLE")
