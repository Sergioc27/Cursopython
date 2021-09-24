# Programa que pide un valor en grados centigrados y lo muestra en grado faherenheit
#0 °C × 9/5) + 32 = 32 °F = formula
grados_celcius = input("Ingresa el Valor en °C ")

grados_celcius = float(grados_celcius)

grados_faherenheit = ((grados_celcius * (9/5)) + 32)

print (f"El equivalente de {grados_celcius}°C es de {grados_faherenheit}")
