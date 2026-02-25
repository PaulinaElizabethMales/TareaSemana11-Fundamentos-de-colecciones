from modelos.producto import Producto
from servicios.inventario import Inventario


def menu():
    inventario = Inventario()
    inventario.cargar_de_archivo()

    while True:
        print("-------------------------------------------")
        print("---- Sistema de Gestión de Inventarios ----")
        print("-------------------------------------------")
        print("[1] Agregar producto")
        print("[2] Eliminar producto")
        print("[3] Actualizar producto")
        print("[4] Buscar producto por nombre")
        print("[5] Mostrar todos los productos")
        print("[6] Guardar inventario")
        print("[7] Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                if not nombre.isalpha():
                    print("Error: El nombre debe contener solo letras.")
                    continue

                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio (número decimal): "))
                inventario.agregar_producto(nombre, cantidad, precio)

            except ValueError:
                print("Error: Debes ingresar valores numéricos válidos en cantidad y precio.")
        elif opcion == "2":
            try:
                id = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        elif opcion == "3":
            try:
                id = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")
                inventario.actualizar_producto(
                    id,
                    cantidad=int(cantidad) if cantidad else None,
                    precio=float(precio) if precio else None
                )
            except ValueError:
                print("Error: Ingresa valores numéricos válidos para cantidad y precio.")

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontró el producto.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()

        elif opcion == "7":
            inventario.guardar_en_archivo()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
