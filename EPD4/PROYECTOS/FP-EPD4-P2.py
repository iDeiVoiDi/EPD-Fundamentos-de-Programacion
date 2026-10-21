print("\n|| Ordenador de precios ||\n")

# === VARIABLES ===
# Marcamos las variables
empresa = ["ProductoA:500,450,600,550", "ProductoB:300,320,310,330", "ProductoC:800,850,750,820"]
productos = []
precios = []
total = [0, 0, 0]

# === LOGICA ===
# Sacamos los datos
for i in empresa:
    productos.append(i.split(":")[0])
    precios.append(i.split(":")[1].split(","))

# Sacamos el total
for i in range(len(precios)):
    for j in range(len(precios[i])):
        total[i] += int(precios[i][j])

# Ordenamos por producto
intercambios = True
n = len(total)
while n > 0 and intercambios:
    intercambios = False
    for i in range(0, n - 1):
        if total[i] < total[i + 1]:
            total[i], total[i + 1] = total[i + 1], total[i]
            productos[i], productos[i + 1] = productos[i + 1], productos[i]
            precios[i], precios[i + 1] = precios[i + 1], precios[i]
            intercambios = True
    n -= 1

# Ordenamos los precios
intercambios = True
n = len(precios[0])
while n > 0 and intercambios:
    intercambios = False
    for i in range(len(precios)):
        for j in range(0, n - 1):
            if precios[i][j] < precios[i][j + 1]:
                precios[i][j], precios[i][j + 1] = precios[i][j + 1], precios[i][j]
                intercambios = True
    n -= 1

print(productos)
print(total)
print(precios)