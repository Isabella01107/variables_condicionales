# Calculadora de descuentos en tienda
# Aplica un descuento según el rango de precio y uno adicional si el cliente tiene tarjeta de fidelidad.

# Pedimos el precio del producto
precio = float(input("Ingrese el precio: "))

# Inicializamos la variable descuento en 0
descuento = 0  

# Determinamos el descuento según el rango de precio
if precio > 100000:
    descuento = 0.15
    resultado = precio * (1 - descuento)
    print("Su precio con descuento es:", resultado)

elif 50000 <= precio <= 100000:
    descuento = 0.10
    resultado = precio * (1 - descuento)
    print("Su precio con descuento es:", resultado)

elif 10000 <= precio <= 49999:
    descuento = 0.05
    resultado = precio * (1 - descuento)
    print("Su precio con descuento es:", resultado)

else:
    resultado = precio  # no hay descuento
    print("No tienes descuentos. Su precio es:", resultado)

# Preguntamos si el cliente tiene tarjeta de fidelidad
tarjeta = input("¿Tienes tarjeta de fidelidad? (si/no): ").lower()

if tarjeta == "si":
    # Se aplica un 5% adicional al descuento ya obtenido
    extra = descuento + 0.05
    resultado = precio * (1 - extra)
    print("Su precio final con tarjeta es de:", resultado)

elif tarjeta == "no":
    print("Su precio final es de:", resultado)
# si los datos no son validos se muestra el mensaje de error
else:
    print("Dato no válido")
