#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el
#capital obtenido en la inversión cada año que dura la inversión.

anual = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años= int(input("¿Años?"))
for i in range(años):
   anual *= 1 + interes / 100
print("Capital tras " + str(i+1) + " años: " + str(round(anual, 2)))