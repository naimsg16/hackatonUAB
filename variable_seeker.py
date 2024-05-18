import re

def find_variables(code_string):
    # Define the regular expression pattern for variable names
    pattern = r'(?<![."\'\w])\b[\w][\w]*\b'
    
    # List of Python reserved keywords
    reserved_keywords = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 
        'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
        'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
        'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
        'raise', 'return', 'try', 'while', 'with', 'yield', 'int', 'list','bool', 'str',
        'set', 'dict', 'tuple', 'float', 'self', 'sum', 'print', 'any', 'all', 'max', 'len', 
        'min', 'sorted', 'reversed', 'enumerate', 'filter', 'map', 'zip', '__name__'
    }

    # Find all matches in the code string
    matches = re.findall(pattern, code_string, re.UNICODE)
    
    # Filter out reserved keywords
    variables = [word for word in matches if word not in reserved_keywords]
    
    variables2 = set(variables)
    return variables2

# Example usage
code_string = """
import random

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al inventario.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                print(f"Producto '{producto.nombre}' eliminado del inventario.")
                return
        print(f"No se encontró el producto con ID {id_producto}.")

    def ver_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for producto in self.productos:
                print(producto)

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                producto.cantidad = nueva_cantidad
                print(f"Cantidad del producto '{producto.nombre}' actualizada a {nueva_cantidad}.")
                return
        print(f"No se encontró el producto con ID {id_producto}.")

    def total_valor_inventario(self):
        total = sum(producto.cantidad * producto.precio for producto in self.productos)
        print(f"Valor total del inventario: ${total:.2f}")

def generar_id_producto():
    return random.randint(1000, 9999)

def main():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Ver inventario")
        print("4. Actualizar cantidad de producto")
        print("5. Ver valor total del inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            id_producto = generar_id_producto()
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            inventario.ver_inventario()
        elif opcion == "4":
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, nueva_cantidad)
        elif opcion == "5":
            inventario.total_valor_inventario()
        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventario.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

"""
