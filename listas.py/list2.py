# programa que pregunte al usuario los números ganadores de la lotería 
#y los almacene en una lista y
#los muestre por pantalla ordenados de menor a mayor.

ganador = []
for i in range(6):
   ganador.append(int(input("Introduce un número ganador: ")))
ganador.sort()
print("Los números ganadores son " + str(ganador))