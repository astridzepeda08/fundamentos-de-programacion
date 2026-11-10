'''
Programa para estudiar los elementos del lenguaje de programacion de Python
Mi nombre es Astrid Valentina Zepeda
'''


nombre = "Ana" #Variable tipo String
edad = 19 #variable tipo integer
estatura = 1.65 #Variable tipo int
es_estudiante = True #Variable tipo booleanas

#Imprimimos la variable y su tipo de dato
print("Nombre:", nombre, type(nombre))
print("Edad:", edad, type(edad))
print("Estatura:", estatura, type(estatura))
print("Estudiante:", es_estudiante, type(es_estudiante))

PROMEDIO_MINIMO = 6

#Introducimos datos y los guardamos en las variables materia y calificacion
materia = input("¿Que materia cursas? ")
calificacion = float(input("¿Que calificacion tienes? "))

#hacemos operaciones basicas
suma = 8 + 2 
resto = 10 % 3
potencia = 2 ** 3

#Estamos declarando dos variables de tipo booleanas 
mayor_de_edad = edad >= 18
aprobado = calificacion >= PROMEDIO_MINIMO and es_estudiante

# Imprimimos el resultado 
print("Suma:", suma, "| Resto:", resto, "| Potencia:", potencia)
print("¿Mayor de edad?", mayor_de_edad)