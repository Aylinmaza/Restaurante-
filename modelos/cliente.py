# Clase Cliente: representa un cliente del restaurante
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []  # lista de productos pedidos

    def agregar_pedido(self, producto):
        self.pedidos.append(producto)

    def calcular_total(self):
        return sum([p.precio for p in self.pedidos])

    def mostrar_informacion(self):
        pedidos_texto = ", ".join([p.titulo for p in self.pedidos])
        return f"Cliente: {self.nombre} | Pedidos: {pedidos_texto}"

    def __str__(self):
        return f"{self.nombre} - Total: ${self.calcular_total():.2f}"
