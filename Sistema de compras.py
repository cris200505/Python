class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def obtener_precio(self):
        return self._precio

    def __str__(self):
        return f"{self._nombre}: ${self._precio}"

class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla 

    def __str__(self):
        return f"Camisa {self._nombre} ({self._talla}): ${self._precio}"

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def __str__(self):
        return f"Pantalón {self._nombre} ({self._talla}): ${self._precio}"

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def __str__(self):
        return f"Zapato {self._nombre} ({self._talla}): ${self._precio}"

class Categoria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        print(f"Categoría: {self._nombre}")
        for producto in self._productos:
            print(producto)

class Tienda:
    def __init__(self):
        self._categorias = []

    def agregar_categoria(self, categoria):
        self._categorias.append(categoria)

    def mostrar_categorias(self):
        for categoria in self._categorias:
            categoria.mostrar_productos()

    def procesar_compra(self, productos_seleccionados):
        total = sum(producto.obtener_precio() for producto in productos_seleccionados)
        print(f"Total a pagar: ${total:.2f}")


camisa1 = Camisa("Camisa Blanca", 29.99, "M")
pantalon1 = Pantalon("Pantalón Negro", 49.99, "L")
zapato1 = Zapato("Zapato Deportivo", 89.99, "42")

categoria_ropa = Categoria("Ropa")
categoria_calzado = Categoria("Calzado")

categoria_ropa.agregar_producto(camisa1)
categoria_ropa.agregar_producto(pantalon1)
categoria_calzado.agregar_producto(zapato1)

tienda = Tienda()
tienda.agregar_categoria(categoria_ropa)
tienda.agregar_categoria(categoria_calzado)

tienda.mostrar_categorias()


productos_a_comprar = [camisa1, pantalon1] 
tienda.procesar_compra(productos_a_comprar)
