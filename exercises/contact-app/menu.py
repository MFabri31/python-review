import os

os.system('cls')
print('====== Bienvenido ===== ')


def add_contact():
    print('Agregar contacto: ')
    pass


def list_contacts():
    print('Listar contactos: ')
    pass


def search_contact():
    print('Buscar contacto: ')
    pass

def delete_contact():
    print('Eliminar contacto: ')
    pass

def exit():
    print('Saliendo... ')
    pass





while True:
    
    print(
    "Agregar contacto [1]\n"
    "Listar contactos [2]\n"
    "Buscar contacto [3]\n"
    "Eliminar contacto [4]\n"
    "Salir [5]"
    )
    option = int(input('Ingrese una opción: >'))
    
    os.system('cls')
    
    if option == 1:
        add_contact()
    if option == 2:
        list_contacts()
    if option == 3:
        search_contact()
    if option == 4:
        delete_contact()
    
    if option == 5:
        exit()
        break


