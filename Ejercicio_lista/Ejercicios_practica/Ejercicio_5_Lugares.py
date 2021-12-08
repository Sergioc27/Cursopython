
#Parte 5.1 lista ordenada
lugares = ["Japon", "Belgica", "Noruega", "Korea", "Rusia"]
print ("Original")
print (", ".join (lugares))
print("Lista ordenada")
print (", ".join (sorted( ["Japon", "Belgica", "Noruega", "Korea", "Rusia"])))
print ("lista sin modificar")
print (", ".join (lugares))

#parte 5.2
print(", ".join(sorted(lugares, reverse = True)))
print (", ".join(lugares))
#Parte 5.3
lugares.reverse()
print (", ".join (lugares))

lugares.reverse()
print(", ".join(lugares))

lugares.sort(reverse= False)
print(", ".join (lugares))

lugares.sort(reverse = True)
print(", ".join(lugares))
