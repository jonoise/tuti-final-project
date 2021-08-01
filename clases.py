from math import prod
from utilidades import Color, Notificacion
from shortuuid import uuid


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cantidades_por_tipo = {}

        self.categorias = ['Pintura', 'Maderas', 'Herramientas', 'Construcción',
                           'Acabados', 'Jardín', 'Decoración', 'Iluminación', 'Automotriz', 'Ferretería']
        self.map_categorias = {
            1: 'pintura',
            2: "maderas",
            3: 'herramientas',
            4: 'construccion',
            5: 'acabados',
            6: 'jardin',
            7: 'decoracion',
            8: 'iluminacion',
            9: 'automotriz',
            10: 'ferreteria',
        }

    def agregar_cantidad_por_tipo(self, producto):
        try:
            self.cantidades_por_tipo[producto.tipo] += producto.cantidad
        except KeyError:
            self.cantidades_por_tipo[producto.tipo] = producto.cantidad

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto
        self.agregar_cantidad_por_tipo(producto)

    def sacar_productos(self, producto, cantidad_salida):
        nueva_cantidad = producto.cantidad - cantidad_salida
        if nueva_cantidad <= 10:
            Notificacion.imprimir_error(
                "No podemos sacar esa cantidad. Ingresa más inventario de ese producto o intenta una salida de menor cantidad")
            return False
        producto.cantidad = nueva_cantidad
        self.cantidades_por_tipo[producto.tipo.lower(
        )] = self.cantidades_por_tipo[producto.tipo.lower()] - cantidad_salida
        return True

    def buscar_producto(self, id):
        try:
            return self.productos[id]
        except KeyError:
            return False

    def cantidad_total(self):
        total = 0
        for _ in self.productos:
            total += 1
        return total

    def cantidad_por_categoria(self, categoria_seleccionada):
        cantidad = 0

        for producto in self.productos.values():
            if producto.categoria == categoria_seleccionada:
                cantidad += 1
        return cantidad

    def despleglar_productos(self):
        productos = []

        for prod in self.productos.values():
            productos.append(prod)
            print(f'\tID: {prod.id} -> {prod.nombre.capitalize()}')

        if len(productos) == 0:
            print(f"\n\t{Color.ERROR}No hay productos en el inventario.\n")

    def despleglar_tipos(self):
        tipos = []

        for index, prod in enumerate(self.productos.values()):
            if prod.tipo.lower() not in tipos:
                tipos.append(prod.tipo.lower())
                print(f'\t{index + 1}. {prod.tipo.capitalize()}')
        if len(tipos) == 0:
            return False
        return tipos

    def despleglar_categorias(self):
        for index, categoria in enumerate(self.categorias):
            print(f'\t{index + 1}. {categoria}')
        print("")

    def seleccionar_categoria(self, opcion):
        try:
            return self.map_categorias[opcion]
        except KeyError:
            return False

    def obtener_reabastecimiento_inmediato(self):
        cantidad_productos = 0
        for prod in self.productos.values():
            if prod.cantidad <= 10:
                cantidad_productos += 1
                print(
                    f"\tID: {prod.id}, nombre: {prod.nombre}, cantidad: {Color.ERROR}{prod.cantidad}{Color.RESET}")
        if cantidad_productos == 0:
            print("Ningún producto necesita reabastecerse urgentemente.")

    def productos_entre_10_y_50(self):
        cantidad_productos = 0
        for prod in self.productos.values():
            if 10 < prod.cantidad <= 50:
                cantidad_productos += 1
                print(
                    f"\tID: {prod.id}, nombre: {prod.nombre}, cantidad: {Color.CUIDADO}{prod.cantidad}{Color.RESET}")
        if cantidad_productos == 0:
            print("No encontramos ningún producto que cumpla con lo establecido.")

    def productos_entre_50_y_100(self):
        cantidad_productos = 0
        for prod in self.productos.values():
            if 50 < prod.cantidad <= 100:
                cantidad_productos += 1
                print(
                    f"\tID: {prod.id}, nombre: {prod.nombre}, cantidad: {Color.EXITO}{prod.cantidad}{Color.RESET}")
        if cantidad_productos == 0:
            print("No encontramos ningún producto que cumpla con lo establecido.")

    def obtener_cantidad_tipo(self, tipo):
        try:
            return self.cantidades_por_tipo[tipo]
        except KeyError:
            return 'No tenemos productos de ese tipo.'

    def obtener_cantidad_categoria(self, categoria):
        try:
            return self.cantidades_por_categoria[categoria]
        except KeyError:
            return 'No tenemos productos de esa categoría.'


class Producto:
    def __init__(self,
                 nombre=None,
                 tipo=None,
                 categoria=None,
                 cantidad=None,
                 precio=None,
                 dimensiones={"altura": None, "anchura": None},
                 marca=None):
        self.id = uuid()
        self.nombre = nombre
        self.tipo = tipo
        self.categoria = categoria
        self.cantidad = int(cantidad)
        self.precio = precio
        self.dimensiones = dimensiones
        self.marca = marca

    def cambiar_atributo(self, attr, valor):
        try:
            self.__dict__[attr] = valor
        except KeyError:
            pass
