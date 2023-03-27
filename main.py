from productos import Productos # Importa el modulo Productos
from tiendas import Tiendas # Importa el modulo Tiendas
from despensa import Despensa # Importa el modulo Despensa

class Main(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menu(self):
        while True:
            menu = Menus() # Crea un objeto de la clase Menus
            print("1.- Modulo Productos") # Opcion para listar los prodcutos
            print("2.- Modulo Tiendas") # Opcion para insertar un nuevo producto
            print("3.- Modulo Despensa") # Opcion para buscar productos por SKU
            print("s.- salir") # Opcion para buscar productos por SKU
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":  # Valida si la opcion elegida es el 1
                menu.menuProductos() # LLama al menuProductos a traves del objeto menu
            elif opcion == "2":  # Valida si la opcion elegida es el 2
                menu.menuTiendas() # LLama al menuTiendas a traves del objeto menu
            elif opcion == "3":  # Valida si la opcion elegida es el 3
                menu.menuProductos() # LLama al menuDespensa a traves del objeto menu
            elif opcion == "s":  # Valida si la opcion elegida es s
                break  # Termina el ciclo while y sale del menu

class Menus():

    def menuProductos(self): # Metodo que muestra el menu del sistema
        productos = Productos() # Crea un objeto de la clase Prodcutos
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Listar Productos") # Opcion para listar los prodcutos
            print("1.- Insertar producto") # Opcion para insertar un nuevo producto
            print("2.- Buscar producto por SKU") # Opcion para buscar productos por SKU
            print("3.- Actualizar producto") # Opcion para actualizar un producto
            print("4.- Borrar producto") # Opcion para borrar un producto
            print("s.- Salir") # Opcion para salir del sistema
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                productos.listarProducto() # Llama al metodo listarProductos a traves del objeto productos
            elif opcion == "1": # Valida si la opcion elegida es el 1
                productos.insertarProducto('sku','nombre','unidad')
            elif opcion == "2": # Valida si la opcion elegida es el 2
                productos.buscarProducto('sku') # Llama al metodo insertarProductos a traves del objeto productos
            elif opcion == "3": # Valida si la opcion elegida es el 3
                productos.actualizarProducto('sku', 'nombre','unidad') # Lama al metodo actualizarProductos 
            elif opcion == "4": # Valida si la opcion elegida es el 4
                productos.borrarProducto('sku') # LLama al metodo borrarProductos a traves del objeto productos
            elif opcion == "s": # Valida si la opcion elegida es el 5
                break  # Termina el ciclo while y sale del menu
                print("Salir del programa")

    def menuTiendas(self): # Metodo que muestra el menu del sistema
        tiendas = Tiendas() # Crea un objeto de la clase Tiendas
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Listar Tiendas") # Opcion para listar los prodcutos
            print("1.- Insertar Tiendas") # Opcion para insertar un nuevo producto
            print("2.- Buscar Tienda") # Opcion para buscar buscar
            print("3.- Actualizar Tiendas") # Opcion para actualizar tiendas
            print("4.- Borrar Tiendas") # Opcion para borrar tiendas
            print("s.- Salir") # Opcion para salir del sistema
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                tiendas.listarTiendas() # Llama al metodo listarTiendas a traves del objeto tiendas
            elif opcion == "1": # Valida si la opcion elegida es el 1
                # Llama al aqui al metodo insertarTiendas 
                print("llama al metodo insertarTiendas")
            elif opcion == "2": # Valida si la opcion elegida es el 2
                tiendas.buscarTiendas('id', 'nombre') #Metodo para buscar tiendas
                print("llama al metodo buscarTiendas")
            elif opcion == "3": # Valida si la opcion elegida es el 3
                tiendas.actualizarTiendas('id', 'nombre')
                print("llama al metodo actualizarTiendas")
            elif opcion == "4": # Valida si la opcion elegida es el 4
                tiendas.borrarTienda('id') # # Llama al metodo borrarTiendas a traves del objeto tiendas
            elif opcion == "s": # Valida si la opcion elegida es el 5
                break # Termina el ciclo while y sale del menu
                print("Salir del programa")
    
    def menuDespensa(self): # Metodo que muestra el menu del sistema
        despensa = Despensa() # Crea un objeto de la clase Despensa
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- listar Compras") # Opcion para listar compras
            print("1.- insertar Compra") # Opcion para insertar compra
            print("2.- buscar Compras por Fecha") # Opcion para buscar compras por fecha
            print("3.- borrar Compra") # Opcion para borrar compra
            print("4.- actualizar Compra") # Opcion para actializar compra
            print("5.- valor Minimo del Producto") # Opcion obtener valor minimo
            print("6.- valor Maximo del Producto") # Opcion para obtener valor maximo
            print("s.- Salir") # Opcion para salir del sistema
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                # Llama al metodo listarCompras aqui
                print("Llama al metodo listarCompras ")
            elif opcion == "1": # Valida si la opcion elegida es el 1
                # Llama al metodo insertarCompras aqui
                print("Llama al metodo insertarCompras ")
            elif opcion == "2": # Valida si la opcion elegida es el 2
                # Llama al metodo vuscarCompras aqui
                print("Llama al metodo buscarCompras ")
            elif opcion == "3": # Valida si la opcion elegida es el 3
                # Lama al metodo borrarCompra aqui
                print("Llama al metodo borrarCompra ")
            elif opcion == "4": # Valida si la opcion elegida es el 4
                # LLama al metodo actualizarCompra
                print("Llama al metodo actualizarCompra ")
            elif opcion == "5": # Valida si la opcion elegida es el 4
                # LLama al metodo valorMinimoProducto aqui
                print("Llama al metodo valorMinimoProducto ")
            elif opcion == "6": # Valida si la opcion elegida es el 4
                # LLama al metodo valorMaximoProducto aqui 
                print("Llama al metodo valormaximoProducto ")           
            elif opcion == "s": # Valida si la opcion elegida es el 5
                break # Termina el ciclo while y sale del menu
                print("Salir del programa")  # imprime la confirmacion de salir del programa


if __name__ == "__main__":
    principal = Main() # Crea un objeto de la clase Main
    principal.menu() # Llama al metodo menu a traves del objeto principal

