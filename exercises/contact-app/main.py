import os

os.system('cls')



contacts = [
    {
       "id":1, 
       "name":"user1", 
       "phone":"123245678", 
    }
]


def add_contact():
    print('===== Agregar contacto =====')
    contact_name = input('Nombre: >')
    contact_phone = input('Teléfono: >')
    
    new_contact = {
        "id": len(contacts) + 1,
        "name": contact_name,
        "phone": contact_phone   
    }
    
    contacts.append(new_contact)

def list_contacts():
    
    print('===== Lista de contactos =====')
    for contact in contacts:
        print("=================")
        for k,v in contact.items():
            print(k,v)
            
 
        
    
def search_contact():
    print('Buscar contacto: ')
    search_term = input('Nombre: >')
    
    contact_founded = None
    
    for contact in contacts:
        print("=================")
        for v in contact.values():
            if v == search_term:
                contact_founded = contact
                
    if contact_founded != None:
        for k,v in contact.items():
            print(k,v)
    else:
        print("Contacto no encontrado")
        
    
    

def delete_contact():
    print('Eliminar contacto: ')
    pass

def exit():
    print('Saliendo... ')
    pass





while True:
    
    print('======================= ')
    print('====== Bienvenido ===== ')
    print('======================= ')
    print(
    "[1] Agregar contacto\n"
    "[2] Listar contactos\n"
    "[3] Buscar contacto\n"
    "[4] Eliminar contacto\n"
    "[5] Salir"
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


