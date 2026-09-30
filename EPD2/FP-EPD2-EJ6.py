print("| Tecnica Pomodoro |\n")

# Marco las variables de estado
seguir_trabajando = False
descanso = False
peticion_descanso = False
advertencia = False

# Recolección de los datos del usuario
tiempo = float(input("• ¿Cuanto tiempo de trabajo llevas?: "))

# Lógica del programa
if tiempo < 25:
    seguir_trabajando = True
elif tiempo == 25:
    descanso = True
elif tiempo > 25 and tiempo <= 50:
    seguir_trabajando = True
    peticion_descanso = True
else:
    advertencia = True

# Muestra de los datos obtenidos
print("| Análisis de los datos...")
if seguir_trabajando:
    print("Tu puedes! Tienes que seguir")
    if peticion_descanso:
        print("En poco tocará tu descanso")
elif descanso:
    print("Enorabuena! Has completado un Pomodoro, comienza tu descanso de 5 mins")
elif advertencia:
    print("Cuidado! Llevas mucho sin descansar, toma un descanso de 15 mins")