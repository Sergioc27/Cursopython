

"""lista con algunos presidentes de México"""

presidentes = ["Andres Manuel", "Enrique peña", "Felipe Calderon", "Vicente Fox"]

# for presidente in presidentes: 
#     print(f" Hola {presidente} cuanto dinero te robaste?")
#     print("devuelve el dinero no seas ratero")

# print(list(range (0, 5)))

# for indice in range(0, len(presidentes)):
#     print(presidentes[indice])


# for valor in range(0, 20, 2):
#     print(valor)

# for valor in range(20):
#     print (valor)


# cuadrados =[] 
# for value in range (1, 11):
#     cuadrado = value ** 2 
#     cuadrados.append(cuadrado)
# print(cuadrados)


# digits = list(range(10))
# print(digits)
# print(max(digits))
# print(min(digits))
# print(sum(digits))
# print (sum(digits) / len(digits))

"""Codigo para generar la lista de cuadrados de un rango version 1"""

# cuadrados = []
# for value in  range(1, 11):
#     cuadrado = value ** 2
#     cuadrados.append(cuadrado)
# print(cuadrados)

# """codigo para generar la lista de cuadrados de un rango version 2"""
# cuadrados =  [value ** 2  for value in range (1, 11)]
# print (cuadrados)

"""vaciar una lista"""
# invitados = ["luis", "jose", "adriana", "fernanda", "juan", "maria"]

# while len(invitados) > 2:
#     invitado = invitados.pop()
#     print(f"{invitado} tu ya no estás invitado")
# print(invitados)

# ultimos_presidentes = presidentes [0:2]
# ultimos_presidentes = presidentes [:2]
# ultimos_presidentes = presidentes [2:]
# ultimos_presidentes = presidentes [-1:]
# ultimos_presidentes = presidentes [-1:1]

# print(ultimos_presidentes)

for presidente in presidentes:
    print(f"{presidente} tu ya no eres presidente jaja")
    