# Programa que simula una calculadora básica con operaciones de suma, resta, multiplicación y división

# Se solicita al usuario que ingrese el primer número
numero1 = int(input("Ingresa el primer número:\n "))

# Se solicita al usuario que ingrese el segundo número
numero2 = int(input("Ingresa el segundo número:\n "))

# Menú de opciones: el usuario elige la operación que desea realizar
operacion = int(input("Ingresa la operación que desea:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n"))

# Si la opción es 1, se realiza la suma
if operacion == 1:
    resultado = numero1 + numero2
    print("El resultado es:", resultado)

# Si la opción es 2, se realiza la resta
elif operacion == 2:
    resultado = numero1 - numero2
    print("El resultado es:", resultado)

# Si la opción es 3, se realiza la multiplicación
elif operacion == 3:
    resultado = numero1 * numero2
    print("El resultado es:", resultado)

# Si la opción es 4, se realiza la división
elif operacion == 4:
    # Validamos que el segundo número no sea cero 
    if numero2 == 0:
        print("Error: no se puede dividir por cero")
    else:
        resultado = numero1 / numero2
        print("El resultado es:", resultado)

# Si la opción ingresada no es válida, se muestra un mensaje de error
else:
    print("Dato inválido")