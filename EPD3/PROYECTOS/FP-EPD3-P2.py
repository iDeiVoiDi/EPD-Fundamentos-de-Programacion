print("\n|| Encuesta ||\n")

# === VARIABLES ===
# Marco las constantes del programa
PREGUNTAS = 10
NO_PERMITIDO = [1, 2]

# Marco las variables de estado
consistente = True

# Marco las variables
respuesta = [5] * PREGUNTAS
pasada = 0


# === DATOS/LOGICA ===
# Solo se ejecuta si no supera las vueltas y es consistente
while pasada < PREGUNTAS and consistente:

    respuesta[pasada] = int(input(f'• "Pregunta nº {pasada + 1}": (1-5) '))
    
    if respuesta[pasada] < 1 or respuesta[pasada] > 5: # Mensaje error fuera de los limites
        print("| Valor no valido")
    
    elif respuesta[pasada] in NO_PERMITIDO: # Deja de ser consistente
        consistente = False
        pregunta_fallida = pasada + 1

    else:
        pasada += 1 # Avanzo una vuelta


# === SALIDA ===
print("| Analizando datos...")
if consistente:
    print("| Fuiste consistente en las respuestas")
else:
    print(f"| No fuiste consistente, la incosistencia fue encontrada en la pregunta nº {pregunta_fallida}")