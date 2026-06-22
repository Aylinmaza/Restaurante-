# Sistema de Restaurante en Python
**Nombre completo:** Aylin Maribel Maza Guaman 

## 📌 Descripción del sistema
Este proyecto implementa un sistema básico para administrar un restaurante utilizando **Programación Orientada a Objetos (POO)** en Python.  
El sistema permite:
- Definir productos con su nombre y precio.
- Registrar clientes y sus pedidos.
- Administrar el menú y la lista de clientes desde la clase principal `Restaurante Doña Margarita `.

## 📂 Estructura del proyecto
La organización modular del proyecto se realizó de la siguiente manera:

RESTAURANTE-APP/
├── modelos/
│   ├── producto.py      # Clase Producto
│   ├── cliente.py       # Clase Cliente
│   └── init.py
├── servicios/
│   ├── restaurante.py   # Clase Restaurante
│   └── init.py
├── main.py              # Programa principal
└── README.md            # Documentación del proyecto


- **Carpeta modelos:** contiene las clases que representan las entidades principales (`Producto` y `Cliente`).  
- **Carpeta servicios:** contiene la clase `Restaurante`, que gestiona el menú y los clientes.  
- **main.py:** archivo principal que crea los objetos, organiza la lógica y muestra la información en consola.  
- **README.md:** documentación del proyecto.

## Reflexión
La modularización del software y la separación de responsabilidades son fundamentales para mantener un código claro, reutilizable y fácil de mantener.  
Al dividir el sistema en módulos (`modelos`, `servicios` y `main.py`), se logra que cada parte cumpla una función específica:
- Los **modelos** representan las entidades.  
- Los **servicios** gestionan la lógica de negocio.  
- El **main** coordina la ejecución.  

Este enfoque facilita la comprensión del proyecto, permite escalarlo con nuevas funcionalidades y refleja buenas prácticas de programación orientada a objetos.
