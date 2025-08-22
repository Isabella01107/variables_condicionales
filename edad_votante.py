# Edad mínima para votar según el país
# Este programa verifica si una persona puede votar dependiendo de su edady del país que ingrese. Cada país tiene una edad mínima diferente

# Diccionario con los países y sus edades mínimas para votar
lista_paises = {"argentina":16, "indonesia":17, "colombia":18, "corea del sur":19, "singapur":21}

# Se pide al usuario que ingrese su país
pais= input("ingresa tu pais:(argentina,indonesia,colombia,corea del sur,singapur)")

# Se pide al usuario que ingrese su edad
edad=int(input("ingresa tu edad:"))

# Condicionales para validar la edad según el país
if pais == "argentina":
  if edad>= 16:
    print("puedes votar en argentina")
  else:
    print("no puedes votaren argentina")
elif pais == "indonesia":
  if edad >= 17:
    print("puedes votar en indonesia")
  else:
    print("no puedes votar en indonesia")
elif pais == "colombia":
  if edad >= 18:
    print("puedes votar en colombia")
  else:
    print("no puedes votar en colombia")
elif pais == "corea del sur":
  if edad>= 19:
    print("puedes votar en corea del sur")
  else:
    print("no puedes votar en corea del sur")
elif pais == "singapur":
  if edad>=21:
    print("puedes votar en singapur")
  else:
    print("no puedes votar en singapur")

# Si el país no está en la lista
else:
  print("pais no valido")