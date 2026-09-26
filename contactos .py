
contactos = {"Ana": "0986324576", "Luis": "0945127845", "María": "0968721354"}

while True:
    print("\n1. Agregar  2. Mostrar  3. Eliminar  4. Salir")
    op = input("Opción: ")

    if op == "1":
        n = input("Nombre: "); t = input("Teléfono: ")
        contactos[n] = t
    elif op == "2":
        print(contactos)
    elif op == "3":
        n = input("Nombre a eliminar: ")
        contactos.pop(n, None)
    elif op == "4":
        break
