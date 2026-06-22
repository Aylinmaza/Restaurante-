# Clase Restaurante: servicio principal que gestiona menú y clientes
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.menu.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_menu(self):
        print(f"--- Menú de {self.nombre} ---")
        for producto in self.menu:
            print(producto)

    def mostrar_clientes(self):
        print(f"--- Clientes de {self.nombre} ---")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())
