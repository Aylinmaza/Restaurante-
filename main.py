from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    # Crear restaurante
    restaurante = Restaurante("Doña margarita ")

    # Crear productos y agregarlos al menú
    producto1 = Producto("Pizza hawaiana ", 8.50)
    producto2 = Producto("Hamburguesa Clásica", 6.00)
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)

    # Registrar cliente y pedidos
    cliente1 = Cliente("Aylin Maza")
    cliente1.agregar_pedido(producto1)
    cliente1.agregar_pedido(producto2)
    restaurante.registrar_cliente(cliente1)

    # Mostrar información organizada
    restaurante.mostrar_menu()
    restaurante.mostrar_clientes()

if __name__ == "__main__":
    main()
