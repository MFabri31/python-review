# Ejer 5
import os


os.system("cls" if os.name == "nt" else "clear")

try:
    number_1 = int(input('Ingrese un número:\n>'))
    number_2 = int(input('Ingrese otro número:\n>'))

    quotient = number_1 // number_2
    residue = number_1 % number_2

    print("Cociente:",quotient)
    print("Resto:",residue)
except:
    print('Solo se permite el ingreso de valores númericos')
