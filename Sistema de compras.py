class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  
        self._precio = precio  

    def obtener_precio(self):
        return self._precio

    def mostrar_info(self):
        return f"{self._nombre}: ${self._precio}"

class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla  

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Talla: {self._talla}"

class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla) 
        self._tipo_tela = tipo_tela  

    def mostrar_info(self):
        return f"Camisa {super().mostrar_info()} - Tipo de tela: {self._tipo_tela}"

class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_pantalon):
        super().__init__(nombre, precio, talla)  
        self._tipo_pantalon = tipo_pantalon  

    def mostrar_info(self):
        return f"Pantalón {super().mostrar_info()} - Tipo: {self._tipo_pantalon}"

class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_zapato):
        super().__init__(nombre, precio, talla)  
        self._tipo_zapato = tipo_zapato  

    def mostrar_info(self):
        return f"Zapato {super().mostrar_info()} - Tipo: {self._tipo_zapato}"

class Carrito:
    def __init__(self):
        self._productos = []  

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        return sum(producto.obtener_precio() for producto in self._productos)

    def mostrar_compra(self):
        for producto in self._productos:
            print(producto.mostrar_info())
        print(f"Total a pagar: ${self.calcular_total():.2f}")

class Tienda:
    def __init__(self):
        self._productos_disponibles = []  

    def agregar_producto(self, producto):
        self._productos_disponibles.append(producto)

    def mostrar_productos(self):
        print("Productos disponibles:")
        for idx, producto in enumerate(self._productos_disponibles):
            print(f"{idx + 1}. {producto.mostrar_info()}")

    def procesar_compra(self):
        carrito = Carrito()
        while True:
            self.mostrar_productos()
            seleccion = input("Selecciona un producto (o 'salir' para finalizar): ")
            if seleccion.lower() == 'salir':
                break
            try:
                indice = int(seleccion) - 1
                if 0 <= indice < len(self._productos_disponibles):
                    carrito.agregar_producto(self._productos_disponibles[indice])
                    print("Producto agregado al carrito.")
                else:
                    print("Selección inválida. Inténtalo de nuevo.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        print("\nResumen de la compra:")
        carrito.mostrar_compra()

if __name__ == "__main__":

    camisa1 = Camisa("Camisa Blanca", 29.99, "M", "Algodón")
    pantalon1 = Pantalon("Pantalón Negro", 49.99, "L", "Chino")
    zapato1 = Zapato("Zapato Deportivo", 89.99, "42", "Deportivo")

    tienda = Tienda()
    tienda.agregar_producto(camisa1)
    tienda.agregar_producto(pantalon1)
    tienda.agregar_producto(zapato1)


    tienda.procesar_compra()
