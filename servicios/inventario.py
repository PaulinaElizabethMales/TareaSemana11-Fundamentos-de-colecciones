import os
import json
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo="servicios/inventario.txt"):
        # USO DE DICCIONARIOS
        self.productos = {}
        # USO DE CONJUNTOS
        self.nombres = set()
        self.archivo = archivo
        self.next_id = 1
        self.cargar_de_archivo()

    def agregar_producto(self, nombre, cantidad, precio):
        if nombre.lower() in self.nombres:
            print("Ya existe un producto con ese nombre.")
            return
        producto = Producto(self.next_id, nombre, cantidad, precio)
        self.productos[self.next_id] = producto
        self.nombres.add(nombre.lower())
        self.next_id += 1
        self.guardar_en_archivo()
        print(f"Producto agregado correctamente: {producto.id}")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_en_archivo()
            print("Producto eliminado y archivo actualizado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado y archivo sincronizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # USO DE LISTAS
        encontrados = [p for p in self.productos.values() if p.get_nombre().lower() == nombre.lower()]
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        for producto in self.productos.values():
            print(producto)

    # -------------------------------
    # SERIALIZACION
    # -------------------------------
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump({id: vars(p) for id, p in self.productos.items()}, f)
            print("Inventario guardado.")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")
    # -------------------------------
    # DESERIALIZACION
    # -------------------------------
    def cargar_de_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                # Si no existe, se crea vacío
                with open(self.archivo, "w") as f:
                    json.dump({}, f)
                self.productos = {}
                self.next_id = 1  # inicializa el contador
                print("Archivo no encontrado, se creó uno nuevo vacío.")
                return

            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.productos = {int(id): Producto(**info) for id, info in datos.items()}
            print("Inventario cargado.")
            if self.productos:
                self.next_id = max(self.productos.keys()) + 1
            else:
                self.next_id = 1

        except Exception as e:
            print(f"Error al cargar inventario: {e}")
