class Color:
    EXITO = '\033[92m'
    CUIDADO = '\033[93m'
    ERROR = '\033[91m'
    RESET = '\033[0m'


class Notificacion:

    @staticmethod
    def imprimir_confirmacion(mensaje):
        # Esta funcion imprime un mensaje en verde.
        # Luego resetea el color al default.
        print(f'{Color.EXITO}{mensaje}{Color.RESET}')
        return True

    @staticmethod
    def imprimir_error(mensaje):
        # Esta funcion imprime un mensaje en rojo.
        # Luego resetea el color al default.
        print(f'{Color.ERROR}{mensaje}{Color.RESET}')
        return False


class Menu:
    @staticmethod
    def saludo():
        print(f"""
    {Color.EXITO}Bienvenid@ al sistema de inventario de la Ferretería 3B.{Color.RESET}
        """)

    @staticmethod
    def menu_de_entrada():
        print(f"""
    Por favor, a continuación ingrese {Color.CUIDADO}el número{Color.RESET} de una opción:
        
    1. Agregar producto al inventario.
    2. Sacar producto del inventario.
    3. Existencias.
    4. Salir. 
        """)

    @staticmethod
    def intro_opcion(opcion):
        regresar_instruccion = f"Si deseas volver al menú principal escribe: {Color.ERROR}regresar{Color.RESET}"
        if opcion == 1:
            texto_corto = "Elegiste agregar un producto al inventario."
            texto_largo = f"""    A continuación elige la categoría que mejor se adapte al producto:
    {regresar_instruccion}
    """
        if opcion == 2:
            texto_corto = "Elegiste sacar un producto del inventario."
            texto_largo = f"""    A continuación elige la opción que desees:
    Si deseas volver al menú principal escribe: {Color.ERROR}regresar{Color.RESET}
    """
        if opcion == 3:
            texto_corto = "Elegiste revisar las existencias del inventario."
            texto_largo = f"""    A continuación elige la opción que desees:
    Si deseas volver al menú principal escribe: {Color.ERROR}regresar{Color.RESET}
    """

        print(f"""
    {texto_corto}""")
        print(texto_largo)

    @staticmethod
    def nuevo_producto():
        print(f"""
    Por favor, ingresa la siguiente información relacionada al producto:
    """)

    @staticmethod
    def repasar_producto(cantidad_categoria):
        print(f"""
        La categoría tiene {cantidad_categoria} producto{"" if cantidad_categoria == 1 else "s"}. 
        Deseas repasar la lista de productos?
        """)

    @staticmethod
    def confirmar_categoria(categoria_seleccionada):
        print(f"""
    {Color.EXITO}Excelente{Color.RESET}, la categoría que seleccionaste fue {Color.EXITO}{categoria_seleccionada.upper()}{Color.RESET}.""")

    @staticmethod
    def existencias_intro():
        print("""
    Elegiste revisar las existencias del inventario.""")
        print(f"""    A continuación elige la opción que desees:

    """)

    @staticmethod
    def sacar_producto_opciones():
        opciones = [
            '\t1. Buscar producto por ID.\n',
        ]
        for op in opciones:
            print(op)

    @staticmethod
    def existencias_opciones():
        opciones = [
            '\t1. Productos para reabastecimiento inmediato.',
            '\t2. Productos cuya cantidad es mayor que 10 y menor o igual que 50.',
            '\t3. Productos cuya cantidad es mayor que 50 y menor o igual que 100.',
            '\t4. Buscar producto por ID.',
            '\t5. Cantidad de productos por tipo.\n',
        ]
        for op in opciones:
            print(op)

    @staticmethod
    def mostrar_cantidad_por_tipo(tipo_seleccionado, cantidad_por_tipo):
        print(f"\n\t{Color.EXITO}★{Color.RESET} Hay {cantidad_por_tipo} productos del tipo {tipo_seleccionado.capitalize()}.\n")
        pass

    @staticmethod
    def mostrar_informacion_producto(producto):
        try:
            print(f"""
        Hemos encontrado el producto {producto.nombre}.
        Cantidad: {producto.cantidad} unidades.
        Precio por unidad: {producto.precio}
        Tipo: {producto.tipo}.
        Categoría: {producto.categoria}
        Dimensiones: Altura > {producto.dimensiones['altura']} cm. Anchura > {producto.dimensiones['anchura']} cm. 
        Marca: {producto.marca}
        """)
        except AttributeError:
            print(f"""
        Hemos encontrado el producto {producto.nombre}.
        Cantidad: {producto.cantidad} unidades.
        Precio por unidad: {producto.precio}
        Tipo: {producto.tipo}.
        Categoría: {producto.categoria}
        Dimensiones: Altura > {producto.dimensiones['altura']} cm. Anchura > {producto.dimensiones['anchura']} cm. 
        Marca: {producto.marca}
        """)


class Validacion:
    @staticmethod
    def validar_menu_de_entrada():
        try:
            opcion = int(
                input(f"{Color.EXITO}Menu principal{Color.RESET} > Elija una opción: "))
            if opcion > 4 or opcion <= 0:
                raise TypeError
            return opcion

        except TypeError:
            Menu.menu_de_entrada()
            Notificacion.imprimir_error("Ingrese un número válido.")
            return False

        except ValueError:
            Menu.menu_de_entrada()
            Notificacion.imprimir_error("Ingrese un valor numeral.")
            return False

    @staticmethod
    def validar_tipos(tipos_validos):
        while True:
            try:
                opcion = int(input(
                    f"{Color.EXITO}Existencias{Color.RESET} > Elija un tipo: "))

                if opcion <= 0 or opcion > len(tipos_validos):
                    raise TypeError
                return opcion

            except TypeError:
                Notificacion.imprimir_error("Ingrese un tipo válido.")

            except ValueError:
                Notificacion.imprimir_error("Ingrese un valor numeral.")

    @staticmethod
    def validar_categoria():
        try:
            opcion = input(
                f"{Color.EXITO}Agregar producto{Color.RESET} > Elija una categoría: ")
            if opcion == 'regresar':
                Menu.menu_de_entrada()
                return opcion

            opcion = int(opcion)
            if opcion > 10 or opcion <= 0:
                raise TypeError
            return opcion

        except TypeError:
            Notificacion.imprimir_error("Ingrese una categoría válida.")
            return False

        except ValueError:
            Notificacion.imprimir_error("Ingrese un valor numeral.")
            return False

    @staticmethod
    def validar_salida_de_producto():
        try:
            opcion = input(
                f"{Color.EXITO}Sacar producto{Color.RESET} > Elija una opción: ")
            if opcion == 'regresar':
                Menu.menu_de_entrada()
                return opcion

            opcion = int(opcion)
            if opcion > 1 or opcion <= 0:
                raise TypeError
            return opcion

        except TypeError:
            Notificacion.imprimir_error("Ingrese una opción válida.")
            return False

        except ValueError:
            Notificacion.imprimir_error("Ingrese un valor numeral.")
            return False

    @staticmethod
    def validar_existencia():
        try:
            opcion = input(
                f"{Color.EXITO}Existencias{Color.RESET} > Elija una opción: ")
            if opcion == 'regresar':
                Menu.menu_de_entrada()
                return opcion

            opcion = int(opcion)
            if opcion > 5 or opcion <= 0:
                raise TypeError
            return opcion

        except TypeError:
            Notificacion.imprimir_error("Ingrese una opción válida.")
            return False

        except ValueError:
            Notificacion.imprimir_error("Ingrese un valor numeral.")
            return False

    @staticmethod
    def validar_numero(tipo):
        numero = None
        while True:
            try:
                numero = float(input(f"{tipo.capitalize()}: "))
                break

            except ValueError:
                Notificacion.imprimir_error("Ingrese un valor numeral.")

        if numero:
            return numero

    @staticmethod
    def validar_dimensiones():
        dimensiones = {"altura": None, "anchura": None}

        while True:
            altura = Validacion.validar_numero("altura en centímetros")
            anchura = Validacion.validar_numero("anchura en centímetros")
            dimensiones["altura"] = altura
            dimensiones["anchura"] = anchura

            if dimensiones["altura"] and dimensiones['anchura']:
                return dimensiones

    @staticmethod
    def validar_entrada_nuevo_producto():
        while True:
            try:
                opcion = input("Deseas agregar otro producto? (s/n): ")
                print(opcion == "s")
                if opcion == "s":
                    Menu.intro_opcion(1)
                    return True
                if opcion == "n":
                    Menu.menu_de_entrada()
                    return False
                raise ValueError
            except ValueError:
                print(
                    f"{Color.ERROR}Debes ingresar sólo la letra 's' (ese) para afirmar, o la letra 'n' (ene) para negar.{Color.RESET}")

    @staticmethod
    def validar_existencia():
        try:
            opcion = input(
                f"{Color.EXITO}Existencias{Color.RESET} > Elija una opción: ")
            if opcion == 'regresar':
                Menu.menu_de_entrada()
                return opcion

            opcion = int(opcion)
            if opcion > 5 or opcion <= 0:
                raise TypeError
            return opcion

        except TypeError:
            Notificacion.imprimir_error("Ingrese una opción válida.")
            return False

        except ValueError:
            Notificacion.imprimir_error("Ingrese un valor numeral.")
            return False
