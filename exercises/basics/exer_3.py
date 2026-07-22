# Ejer 2


try:
    user_age = int(input('Ingrese su edad:\n>'))
    
    if user_age <= 0 or user_age > 99:
        print("Ingrese una edad válida")
    else:
        print("Edad del usuario: ",user_age, "años")
except:
    print("Solo se acepta el ingreso de valores númericos")
    