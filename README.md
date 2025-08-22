variables_condicionales
# variables_condicionales
Este repositorio contiene 4 programas en Python que utilizan variables y estructuras condicionales para resolver distintos problemas.
## programas inluidos:
### 1.calculadora.py
**descripcion**
simula una calculadora básica con operaciones de suma,resta,multiplicacion y division
**ejemplo**
ingresa numero 1: 4
ingresa numero 2: 3
ingresa tipo de operacion: 1.suma, 2.resta, 3.multiplicacion 4.division
operacion: 3
resultado: 12
**posibles errores**
- division entre 0
- ingresar letras en vez de numeros
### 2.temperatura.py
**descripcion**
Convierte temperaturas entre Celsius, Fahrenheit y Kelvin.
**ejemplo** 
Ingrese el tipo de grados que quieres convertir (Celsius, Kelvin, Fahrenheit): Celsius
Ingrese el valor de la temperatura: 40
Ingrese el tipo de grados al que quieres convertir: Kelvin
Su temperatura en Kelvin es: 313.15
**Posibles errores:**
- Ingresar un tipo de escala inválido.
- Usar mayúsculas o minúsculas diferentes
### 3.edad_votante.py
**descripcion**
Determina si una persona puede votar según su país y edad. Incluye reglas para Argentina, Indonesia, Colombia, Corea del Sur y Singapur.
**ejemplo**
Ingresa tu país (argentina, indonesia, colombia, corea del sur, singapur): singapur
Ingresa tu edad: 20
No puedes votar en Singapur (edad mínima: 21)
**posibles errores**
-  Ingresar un país que no está en la lista.
- Usar otro formato de nombre (mayúsculas/minúsculas).
### 4. descuentos_tienda.py
**descripción:**  
Calcula el precio final de un producto aplicando descuentos:
- > 100,000 → 15% de descuento
- 50,000 a 100,000 → 10%
- 10,000 a 49,999 → 5%
- Tarjeta de fidelidad → +5% adicional
**ejemplo:**
Ingrese el precio del producto: 100000
Su precio con descuento es: 90000.0
¿Tiene tarjeta de fidelidad? (si/no): si
Su precio final con tarjeta es: 85000.0
**Posibles errores**
- Escribir el precio con separador de miles (`100.000` en vez de `100000`).
- Ingresar texto en lugar de números.