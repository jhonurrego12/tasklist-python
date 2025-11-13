productos = ["laptop", "mouse", "teclado", "audifonos", "monitor"]
precios = [2500, 50, 120, 80, 300]
carrito = []

def mostrar_productos():
    print("\nPRODUCTOS DISPONIBLES:")
    for i in range(len(productos)):
        print(f"{i+1}. {productos[i]} - ${precios[i]}")

def agregar_al_carrito():
    mostrar_productos()
    try:
        opcion = int(input("Ingresa el número del producto a comprar: ")) - 1
        if 0 <= opcion < len(productos):
            carrito.append(precios[opcion])
            print(f"{productos[opcion]} agregado al carrito")
        else:
            print("Opción no válida")
    except ValueError:
        print("Debes ingresar un número válido")

def mostrar_total():
    if not carrito:
        print("Carrito vacío")
    else:
        total = sum(carrito)
        print(f"Total a pagar: ${total}")

def menu():
    while True:
        print("\nMENU TIENDA ONLINE TECH")
        print("1. VER PRODUCTOS")
        print("2. AGREGAR PRODUCTO AL CARRITO")
        print("3. VER EL TOTAL A PAGAR")
        print("4. SALIR")
        try:
            opcion = int(input("Digite la opción: "))
            if opcion == 1:
                mostrar_productos()
            elif opcion == 2:
                agregar_al_carrito()
            elif opcion == 3:
                mostrar_total()
            elif opcion == 4:
                print("¡Hasta la próxima!")
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Debes ingresar un número.")
           
menu()