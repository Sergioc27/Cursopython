#6.1 Lista del 0 al 10

lista =[]
contador = 11

while contador > 0:
    lista.insert (0, contador -1)
    contador = contador-1

print(f'Lista Ascendente: {lista}' )

#6.2 Invertir lista sin la función reverse
contador = 1
lista = []
for contador in range(0,11):
    lista.insert(0,contador)

print(f"Lista Descendente: {lista}" )


#6.3 Lista Inversa

lista.reverse()
print(f'Lista Inversa {lista}')





