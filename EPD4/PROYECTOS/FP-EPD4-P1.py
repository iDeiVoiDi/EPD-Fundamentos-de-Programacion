print("\n|| BUSCAMINAS ||\n")

# === VARIABLES ===
# Marcamos las constantes del programa
MINAS = 3
TABLERO = 5

# Marcamos las variables
tabla = [
    ["0"] * TABLERO for _ in range(TABLERO)
]
minas = []
minas_cercanas = 0

# === DATOS ===
# Preguntamos los datos necesarios
print(f"| Tablero {TABLERO}x{TABLERO} empezando en 1 y terminando en {TABLERO} desde abajo a la izquierda")
for i in range(MINAS):
    x = int(input(f"• Donde quieres colocar la mina {i+1} en X?: "))
    y = int(input(f"• Donde quieres colocar la mina {i+1} en Y?: "))
    minas.append([x - 1, TABLERO - y])

# === LOGICA ===
# Colocar las minas
for x, y in minas:
    tabla[y][x] = "M"

# Mapeo de las minas
for y in range(TABLERO):
    for x in range(TABLERO):
        minas_cercanas = 0

        if tabla[y][x] != "M":

            # Fila de arriba
            if y - 1 >= 0:
                if x - 1 >= 0:
                    if tabla[y - 1][x - 1] == "M":
                        minas_cercanas += 1
                if tabla[y - 1][x] == "M":
                    minas_cercanas += 1
                if x + 1 <= (TABLERO - 1):
                    if tabla[y - 1][x + 1] == "M":
                        minas_cercanas += 1

            # Fila de enmedio
            if x - 1 >= 0:
                if tabla[y][x - 1] == "M":
                    minas_cercanas += 1
            if x + 1 <= (TABLERO - 1):
                if tabla[y][x + 1] == "M":
                    minas_cercanas += 1

            # Fila de abajo
            if y + 1 <= (TABLERO - 1):
                if x - 1 >= 0:
                    if tabla[y + 1][x - 1] == "M":
                        minas_cercanas += 1
                if tabla[y + 1][x] == "M":
                    minas_cercanas += 1
                if x + 1 <= (TABLERO - 1):
                    if tabla[y + 1][x + 1] == "M":
                        minas_cercanas += 1
            
            tabla[y][x] = f"{minas_cercanas}"

# === SALIDA ===
print("| Calculando tablero...")

for y in range(TABLERO):
    for x in range(TABLERO):
        print(f"{tabla[y][x]} ", end="")
    print("")

