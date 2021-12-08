#5.1 Pizzas
pizzas = [ 'Meatlover', 'Pepperoni', 'Mexicana']

print (", ".join (pizzas))

pizzas_de_mi_amigo = pizzas [0:3]
print(", ".join (pizzas_de_mi_amigo))

pizzas.append ("Hawaiana")

pizzas_de_mi_amigo.append( "Cuatro quesos")
print (", ".join (pizzas))
print(", ".join (pizzas_de_mi_amigo))
