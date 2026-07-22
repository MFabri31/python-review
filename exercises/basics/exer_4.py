# Ejer 4
import os


os.system('cls')



try:    
    number_1 = int(input('Ingrese un número:\n>'))
    number_2 = int(input('Ingrese otro número:\n>'))
    
    result = number_1 + number_2
    
    print("Rsultado suma:", result)
except:
    print('Valor ingresado incorrecto')


