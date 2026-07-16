import os

os.system('cls')



tasks = [
    {
       "id":1, 
       "name":"task1", 
       "description":"How to connect an python to db...", 
       "is_completed":False
    }
]


def add_task():
    print('===== Agregar tarea =====')
    task_name = input('Título: >')
    task_description = input('Descripción: >')
    
    new_task = {
        "id": len(tasks) + 1,
        "name": task_name,
        "description": task_description,
        "is_completed":False
    }
    
    tasks.append(new_task)

def list_tasks():
    
    print('===== Mis tareas =====')
    for task in tasks:
        print("=================")
        for k,v in task.items():
            print(k,v)
            
     
def search_task():
    print('Buscar tarea: ')
    search_task = input('Título: >')
    
    found_task = None
    
    for task in tasks:
        print("=================")
        for v in task.values():
            if v == search_task:
                found_task = task
                
                
    if found_task is not None:
        for k,v in task.items():
            print(k,v)
    else:
        print("Tarea no encontrado")
        
    
def delete_task():
    print('Eliminar tarea: ')
    search_term = input('Título: >')
    
    found_task = None
    
    for task in tasks:
        print("=================")
        for v in task.values():
            if v == search_term:
                found_task = task
   
    if found_task is not None:
        tasks.remove(found_task)
        print("Tarea eliminado")
    else:
        print("Tarea no encontrado")

def exit():
    print('Saliendo... ')
    pass





while True:
    
    print('======================= ')
    print('====== TODO APP ===== ')
    print('======================= ')
    print(
    "[1] Agregar Tarea\n"
    "[2] Listar Tareas\n"
    "[3] Buscar Tarea\n"
    "[4] Eliminar Tarea\n"
    "[5] Salir"
    )
    
    try:
        option = int(input('Ingrese una opción: >'))
    except ValueError:
        print("Ingrese una opción válida")
        continue
    
    os.system('cls')
    
    if option == 1:
        add_task()
    elif option == 2:
        list_tasks()
    elif option == 3:
        search_task()
    elif option == 4:
        delete_task()
    elif option == 5:
        exit()
        break


