# Listas, funciones, menús y excepciones

tareas = []
nextId = 1  # contador incremental para asignar IDs


def listar():
    if not tareas:
        print("No hay tareas")
        return

    print("\nID | ESTADO | TITULO")
    for t in tareas:
        estado = "OK" if t[2] else "NOT"
        print(f"{t[0]:<3} | {estado:<6} | {t[1]}")


def agregar():
    global nextId

    titulo = input("Título: ").strip()
    if not titulo:
        print("Título vacío")
        return

    tareas.append([nextId, titulo, False])
    nextId += 1
    print("Tarea agregada")


def marcarTarea():
    if not tareas:
        print("No hay tareas")
        return

    try:
        tid = int(input("Id de la tarea a marcar como realizada: ").strip())
    except ValueError:
        print("Id inválido. Digite valores numéricos.")
        return

    for t in tareas:
        if t[0] == tid:
            t[2] = True
            print("Tarea marcada como realizada")
            return

    print("No existe el id")


def eliminar():
    if not tareas:
        print("No hay tareas")
        return

    try:
        tid = int(input("Id de la tarea que desea eliminar: ").strip())
    except ValueError:
        print("Id inválido. Digite valores numéricos.")
        return

    for i, t in enumerate(tareas):
        if t[0] == tid:
            del tareas[i]
            print("Tarea eliminada")
            return

    print("No existe ese id a eliminar")


def menu():
    print("\nTASKLIST")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tareas realizadas")
    print("4. Eliminar tarea")
    print("5. Salir")


# Bucle principal
while True:
    menu()
    op = input("Digite la opción: ").strip()

    if op == "1":
        agregar()
    elif op == "2":
        listar()
    elif op == "3":
        marcarTarea()
    elif op == "4":
        eliminar()
    elif op == "5":
        print("Hasta la próxima...")
        break
    else:
        print("Opción inválida")
