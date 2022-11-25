#programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas,Física,Química,Historia y Lengua)en una lista y la muestre
#por pantalla

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for materia in materias:
  notas = input("¿Qué nota has sacado en " + materia + "?")
notas.append(notas)
for i in range(len(materias)):
   print("En " + materias[i] + " has sacado " + notas[i]) 