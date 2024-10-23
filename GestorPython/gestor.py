# Funciones para gestionar las tareas
def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print(f'Tarea "{tarea}" agregada correctamente.')

def eliminar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        print(f'Tarea "{tarea_eliminada}" eliminada correctamente.')
    else:
        print("Índice no válido. Inténtalo de nuevo.")

def listar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f'{i}. {tarea}')
        print()

def guardar_tareas(tareas, archivo):
    with open(archivo, 'w') as f:
        for tarea in tareas:
            f.write(tarea + '\n')
    print("Tareas guardadas correctamente.")

def cargar_tareas(archivo):
    tareas = []
    try:
        with open(archivo, 'r') as f:
            tareas = f.read().splitlines()
    except FileNotFoundError:
        print("No se encontró el archivo de tareas. Creando uno nuevo.")
    return tareas

# Menú principal
def menu():
    archivo = "tareas.txt"
    tareas = cargar_tareas(archivo)
    
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("4. Guardar y salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            tarea = input("Escribe la nueva tarea: ")
            agregar_tarea(tareas, tarea)
        elif opcion == '2':
            listar_tareas(tareas)
            try:
                indice = int(input("Escribe el número de la tarea a eliminar: ")) - 1
                eliminar_tarea(tareas, indice)
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")
        elif opcion == '3':
            listar_tareas(tareas)
        elif opcion == '4':
            guardar_tareas(tareas, archivo)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
