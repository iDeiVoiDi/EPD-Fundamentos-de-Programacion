print("| Filtro de Contenido |\n")

# Marco las variables de estado
contenido_sensible = False
promocion = False
spam = False 

# Recolección de los datos del usuario
texto = input("• Introduzca el texto de la publicación: ")

# Lógica del programa
if "odio" in texto or "violencia" in texto:
    contenido_sensible = True

if "sorteo" in texto and "gratis" in texto:
    spam = True
elif "sorteo" in texto:
    promocion = True

# Muestra de los datos obtenidos
print("| Análisis del texto...")
if contenido_sensible or promocion or spam:
    if contenido_sensible:
        print("→ ALERTA A CONTENIDO SENSIBLE | Encontrado un 'odio' o 'violencia'")
    if promocion:
        print("→ ALERTA A PROMOCIÓN | Encontrado un 'sorteo'")
    if spam:
        print("→ ALERTA A SPAM | Encontrado un 'sorteo' y 'gratis'")
else:
    print("→ NO HUBO ALERTAS")