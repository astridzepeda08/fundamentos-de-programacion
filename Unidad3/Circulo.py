import math
radio = float(input("Radio del círculo: "))

area = math.pi * math.pow(radio, 2)
perimetro = 2 * math.pi * radio


print("Área: ", round(area, 2))
print("Perímetro: ", round(perimetro, 2))
print("Raíz cuadrada del radio: ", round(math.sqrt(radio), 2))
print("Techo del área: ", math.ceil(area))


'''expliquen con sus palabras como funciona la linea 1.
tmb seleccione dos operaciones de la libreria math y ejecutelas.'''

x = 3
y = 6

pow = math.pow(x, y)
