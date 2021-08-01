from math import prod
from utilidades import Color, Menu, Notificacion, Validacion
from clases import Inventario, Producto


def EjecutarPrograma():
    # Se inicializa el inventario.
    inventario = Inventario()

    Menu.saludo()
    Menu.menu_de_entrada()

    # MENU PRINCIPAL
    while True:
        OPCION = Validacion.validar_menu_de_entrada()

        if OPCION == 1:
            Menu.intro_opcion(OPCION)
            inventario.despleglar_categorias()

            while True:
                indice_categoria = Validacion.validar_categoria()

                # si la opción que usuario ingresa es "regresar"
                if indice_categoria == 'regresar':
                    break

                if indice_categoria:

                    # la categoría en minúsculas:
                    categoria_seleccionada = inventario.seleccionar_categoria(
                        indice_categoria)
                    Menu.confirmar_categoria(categoria_seleccionada)

                    # el número de productos en esa categoría:
                    cantidad_categoria = inventario.cantidad_por_categoria(
                        categoria_seleccionada)

                    # si el número de productos es mayor a 0, preguntamos si quiere revisar los existentes:
                    if cantidad_categoria > 0:
                        Menu.repasar_producto(cantidad_categoria)

                    # Si la categoría está vacía, procedemos a ingresar un producto:
                    Menu.nuevo_producto()

                    # Todos los atributos con .lower():
                    categoria = categoria_seleccionada
                    nombre = input("Nombre: ").lower()
                    tipo = input("Tipo: ").lower()
                    cantidad = Validacion.validar_numero('cantidad')
                    precio = Validacion.validar_numero('precio')
                    dimensiones = Validacion.validar_dimensiones()
                    marca = input("Marca: ").lower()

                    # inicializamos el producto
                    producto = Producto(
                        nombre, tipo, categoria, cantidad, precio, dimensiones, marca)

                    # agregamos el producto
                    inventario.agregar_producto(producto)
                    Notificacion.imprimir_confirmacion(
                        "Producto agregado satisfactoriamente.")

                    # nuevo_producto returns True o False
                    nuevo_producto = Validacion.validar_entrada_nuevo_producto()

                    # si el usuario no quiere agregar otro nuevo_producto, break para ir al menu principal
                    if not nuevo_producto:
                        break
                    # de lo contrario, desplegamos la lista de categorías y vuelve a empezar el loop.
                    inventario.despleglar_categorias()

        if OPCION == 2:
            Menu.intro_opcion(OPCION)
            Menu.sacar_producto_opciones()
            
            while True:
                opcion_sacar_producto = Validacion.validar_salida_de_producto()
                if opcion_sacar_producto == "regresar":
                    break

                if opcion_sacar_producto:
                    print(
                        f"\n\tIngresa el ID del producto que deseas buscar. \n\tSi no conoces el ID, escribe {Color.CUIDADO}'buscar'{Color.RESET} para desplegar la lista completa.\n")

                    id = input("ID: ")
                    if id == 'buscar':
                        print(
                            "\n\tA continuación copie el ID del producto.\n")
                        print(
                            "\n\tY ejecute la opción 1 de nuevo.\n")
                        inventario.despleglar_productos()
                        print('\n')
                    else:
                        producto = inventario.buscar_producto(id)
                        if not producto:
                            print(
                                "Ese producto no existe o fue ingresado incorrectamente.")
                        else:
                            Menu.mostrar_informacion_producto(producto)
                            cantidad_salida = int(input(
                                '\t\nElija la cantidad para la salida: '))
                            producto_actualizado = inventario.sacar_productos(
                                producto, cantidad_salida)

                            if producto_actualizado:
                                Notificacion.imprimir_confirmacion(
                                    "Hemos actualizado la cantidad indicada.")
            pass
        if OPCION == 3:
            """
            REVISAR EXISTENCIAS DEL INVENTARIO
            """
            Menu.intro_opcion(OPCION)
            Menu.existencias_opciones()

            while True:
                opcion_existencia = Validacion.validar_existencia()
                if opcion_existencia == 'regresar':
                    break

                if opcion_existencia:
                    if opcion_existencia == 1:
                        inventario.obtener_reabastecimiento_inmediato()
                    if opcion_existencia == 2:
                        inventario.productos_entre_10_y_50()
                    if opcion_existencia == 3:
                        inventario.productos_entre_50_y_100()
                    if opcion_existencia == 4:
                        print(
                            f"\n\tIngresa el ID del producto que deseas buscar. \n\tSi no conoces el ID, escribe {Color.CUIDADO}'buscar'{Color.RESET} para desplegar la lista completa.\n")

                        id = input("ID: ")
                        if id == 'buscar':
                            print("\n\tEsta es la lista de productos. \n\tCopia el ID y vuelve a ejecutar la opción 4.\n")
                            inventario.despleglar_productos()
                        else:
                            producto = inventario.buscar_producto(id)
                            if not producto:
                                print(
                                    "Ese producto no existe o fue ingresado incorrectamente.")
                            else:
                                Menu.mostrar_informacion_producto(producto)

                    if opcion_existencia == 5:
                        print('\n\tEstos son los tipos de producto disponibles. \nElija el número que desee para verificar su cantidad.')
                        tipos_validos = inventario.despleglar_tipos()

                        if tipos_validos:
                            tipo_seleccionado = Validacion.validar_tipos(
                                tipos_validos
                            )
                            # si la opción que usuario ingresa es "regresar"
                            if tipo_seleccionado == 'regresar':
                                break

                            if tipo_seleccionado:
                                tipo_seleccionado = tipos_validos[tipo_seleccionado - 1]
                                cantidad_por_tipo = inventario.obtener_cantidad_tipo(
                                    tipo_seleccionado
                                )
                                Menu.mostrar_cantidad_por_tipo(
                                    tipo_seleccionado, cantidad_por_tipo
                                )
                        else:
                            print(
                                f'{Color.ERROR}El inventario está vacío. Ingrese un producto primero.{Color.RESET}')
            pass
        if OPCION == 4:
            print("elegiste la opcion 4, bye.")
            break


EjecutarPrograma()
