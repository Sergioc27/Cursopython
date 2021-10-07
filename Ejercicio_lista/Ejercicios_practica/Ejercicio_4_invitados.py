#Ejercicio #4 Invitados
import time

#parte 4.1

nombres = [ 'Johnny Cash', 'George Harrison', 'Kurt Cobain', 'Janis Joplin', 'Jim Morrison', 'Pedro Ruiz', 'Sergio Clara']

print (" ")
print ( f"Hola { nombres[0]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[1]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[2]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[3]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[4]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[5]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
print (" ")
time.sleep(2)
#parte 4.2
print (f" Estimado señor {nombres[6]}, lamento informarle que no podé asistir a su magnánime evento, \ndebido a problemas personales, le agradezco sinceramente su invitacion, \nA T E N T A M E N T E \t\t\t\t\t {nombres[4]}\n ")
time.sleep(2)


nombres [4] = "Homero Simpson"


print ( f"Hola { nombres[0]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[1]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[2]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[3]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[4]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[5]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
print (" ")

time.sleep(2)
#parte 4.3

print("Nos complace informarle que hemos encontrado la manera en que usted puede invitar a 3 personas más, ya que contamos con una mesa que nos permite incrementar el número de sus invitados\n ")

print("Por favor indiquenos los nombres para poder realizar el envío de sus invitaciones personalizadas\n ")

nombres.insert(0, "Paco Mendez")

nombres.insert(3, "Fernando Gonzalez")

nombres.insert(6, "Magaly Zamorano")

nombres.pop()
time.sleep(2)

print(nombres)

print("Perfecto, procederemos a envíar sus invitaciones")
time.sleep(2)
print (" ")
print ( f"Hola { nombres[0]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[1]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[2]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[3]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[4]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[5]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[6]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[7]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
time.sleep(2)
print ( f"Hola { nombres[8]}, estoy realizando una pequeña fiesta y me gustaría contar con su presencia, habrá bebidas refrescantes, botanas y taquitos al vapor. ¡No faltes!\n ")
print (" ")
time.sleep(2)
#Etapa 4.4
print(f"Lamento informarle que por problemas ajenos a mi persona, la mesa que había reservado para mis invitados no está disponle,\npor lo que me veo en la penosa necesidad de reducir mi lista a solo 2 personas.\n ")

print (" ")
print ( f"Hola { nombres.pop(0)}, lamento informarle que por motivos agenos a mi persona me veo en la necesidad de cancelar su invitación a la reunión que habíamos programado. Espero pueda entenderme. Esperemos pronto podamos reunirnos. Agradezco su atencion y me disculpo por las molestias que esto pueda ocasionarle.\n ")
time.sleep(2)
print ( f"Hola { nombres.pop(0)}, lamento informarle que por motivos agenos a mi persona me veo en la necesidad de cancelar su invitación a la reunión que habíamos programado. Espero pueda entenderme. Esperemos pronto podamos reunirnos. Agradezco su atencion y me disculpo por las molestias que esto pueda ocasionarle.\n ")
time.sleep(2)
print ( f"Hola { nombres.pop(0)}, lamento informarle que por motivos agenos a mi persona me veo en la necesidad de cancelar su invitación a la reunión que habíamos programado. Espero pueda entenderme. Esperemos pronto podamos reunirnos. Agradezco su atencion y me disculpo por las molestias que esto pueda ocasionarle.\n ")
time.sleep(2)
print ( f"Hola { nombres.pop(0)}, lamento informarle que por motivos agenos a mi persona me veo en la necesidad de cancelar su invitación a la reunión que habíamos programado. Espero pueda entenderme. Esperemos pronto podamos reunirnos. Agradezco su atencion y me disculpo por las molestias que esto pueda ocasionarle.\n ")
time.sleep(2)
print ( f"Hola { nombres.pop(0)}, lamento informarle que por motivos agenos a mi persona me veo en la necesidad de cancelar su invitación a la reunión que habíamos programado. Espero pueda entenderme. Esperemos pronto podamos reunirnos. Agradezco su atencion y me disculpo por las molestias que esto pueda ocasionarle.\n ")
time.sleep(2)
print ( f"Hola { nombres.pop(0)}, lamento informarle que por motivos agenos a mi persona me veo en la necesidad de cancelar su invitación a la reunión que habíamos programado. Espero pueda entenderme. Esperemos pronto podamos reunirnos. Agradezco su atencion y me disculpo por las molestias que esto pueda ocasionarle.\n ")
time.sleep(2)
print ( f"Hola { nombres.pop(1)},  lamento informarle que por motivos agenos a mi persona me veo en la necesidad de cancelar su invitación a la reunión que habíamos programado. Espero pueda entenderme. Esperemos pronto podamos reunirnos. Agradezco su atencion y me disculpo por las molestias que esto pueda ocasionarle.\n ")
print (" ")
time.sleep(2)

print ( f"Hola { nombres[0]}, me complace informarle que su lugar aún esta confirmado para nuestra reunión lamento las confusión que esto ha provocado, alegraría mucho contar con su presencia.\n")

print ( f"Hola { nombres[1]}, me complace informarle que su lugar aún esta confirmado para nuestra reunión lamento las confusión que esto ha provocado, alegraría mucho contar con su presencia.\n ")
time.sleep(1)

print("Muchas gracias por asistir a la reunion, me complace haberlos visto, y agradezco su paciencia y tiempo")
print("me gustaría saber su opinion de que les parecio la fiesta.")

