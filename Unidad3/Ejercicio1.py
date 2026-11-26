'''Astrid valentina zepeda
modulo 3 '''

calificacion = float(input("escribe tu calificacion: "))

if calificacion >= 6:
    print("Aprobado")
else:
    print("Reprobado")
    
if calificacion >= 9 and calificacion <= 10:
    print("Excelente")

if calificacion < 0 or calificacion > 10:
    print("calificacion invalida")

if calificacion >= 8 and calificacion < 9:
    print("Buen trabajo")
