# Programa: Conversor de temperaturas
# Este programa convierte valores entre Celsius, Kelvin y Fahrenheit.
# El usuario debe ingresar el tipo de grados de origen, el valor numérico y el tipo de grados al que desea convertir.

# Solicitar el tipo de grados inicial al usuario
tipo = input("Ingrese el tipo de grados que quieres convertir (Celsius, Kelvin, Fahrenheit): ")

# Solicitar el valor numérico de la temperatura
valor = float(input("Ingrese el valor de la temperatura: "))

# Solicitar el tipo de grados al que se quiere convertir
conversion = input("Ingrese el tipo de grados al que quieres convertir (Celsius, Kelvin, Fahrenheit): ")

# Verificar si el tipo de grados de origen es Celsius
if tipo == "celsius":
    if conversion == "kelvin":  # Celsius a Kelvin
        operacion = valor + 273.15
        print("Su temperatura en Kelvin es:", operacion)
    elif conversion == "fahrenheit":  # Celsius a Fahrenheit
        operacion = ((9 / 5) * valor) + 32
        print("Su temperatura en Fahrenheit es:", operacion)
    else:
        print("Dato inválido, conversión no válida.")

# Verificar si el tipo de grados de origen es Kelvin
elif tipo == "Kelvin":
    if conversion == "celsius":  # Kelvin a Celsius
        operacion = valor - 273.15
        print("Su temperatura en Celsius es:", operacion)
    elif conversion == "Fahrenheit":  # Kelvin a Fahrenheit
        operacion = ((9 / 5) * (valor - 273.15)) + 32
        print("Su temperatura en Fahrenheit es:", operacion)
    else:
        print("Dato inválido, conversión no válida.")

# Verificar si el tipo de grados de origen es Fahrenheit
elif tipo == "Fahrenheit":
    if conversion == "celsius":  # Fahrenheit a Celsius
        operacion = ((valor - 32) * 5) / 9
        print("Su temperatura en Celsius es:", operacion)
    elif conversion == "kelvin":  # Fahrenheit a Kelvin
        operacion = (((valor - 32) * 5) / 9) + 273.15
        print("Su temperatura en Kelvin es:", operacion)
    else:
        print("Dato inválido, conversión no válida.")

# En caso de que el tipo de grados inicial no sea válido
else:
    print("Dato inválido, tipo de grados no reconocido.")
