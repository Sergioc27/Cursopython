#Crea un programa que pida: Nombre, edad, teléfono dirección, email, y nacionalidad e imprima un mensaje personalizado para el.

nombre= input ("¿Cual es tu nombre?: ")
nombre = str (nombre)
edad = input ("¿Cual es tu edad?: ")
edad = int (edad)
telefono = input ("Podrías proporcionarnos tu numero de teléfono?: ")
telefono = int (telefono)
direccion = input("¿Cual es tu dirección?: ")
direccion = str (direccion)
email = input("Necesitaremos tu email tamien, ¿el cual es?: ")
email = str (email)
nacionalidad = input ("Por último, dinos de donde eres... Nacionaliad: ")
nacionalidad = str (nacionalidad)

print ("Perfecto verificamos tus datos")
print (f" Hola {nombre} me dijisite que tienes {edad} años, tu teléfono es el {telefono}, ademas vives en {direccion} y tu correo electonico es {email}, y veo que eres de {nacionalidad} ")


