
import sys
from typing import Tuple


# lista = []
# mi_tuple = ()
# """ """ 
# print (type(lista))
# print (type(mi_tuple))

# print (f" Tamaño en memoria de la lista: {sys.getsizeof(lista)}")
# print (f" Tamaño en memoria del tuple: {sys.getsizeof(mi_tuple)}")

# """Acceder a los valores de una lista o un tuple por medio de su indice:""" """ """
# list_2 = [1, 2, 3, 4, 5]
# mi_tuple_2 = (6, 7, 8, 9, 10) #El indice de python comienza en de 0

# print(list_2[2])

# print(mi_tuple_2[4])

#Acceder al valor de una lista o tuple.

# print(list_2[-1]) #Los valores negativos son para llamar los numeros de manera intertida de derecha a izquierda
# print(list_2[-2])
# print(list_2[-3])



# print(len(list_2)) #Funcion para revisar la cantidad de items dentro de una variable
# print(len(mi_tuple_2))


#Editar valores de una lista



list_3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
tuple = (10, 11, 12, 13, 14, 15, 16)


list_3[0] = 10

print(list_3)

#Agregar un valor a una lista

list_3.insert(1, 5)
list_3.append("el ultimo")

print(list_3)



