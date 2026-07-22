# Ejer 6
import math

try:
    circle_radio = int(input('Ingrese el radio de un circulo: ')) 
    area = math.pi * circle_radio ** 2
    print(f'Área del círculo: {area:.2f}')
except:
    print('Valor no aceptado.')
    