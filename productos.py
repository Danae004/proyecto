import csv  # Librería para abrir, leer y escribir archivos CSV
from tabulate import tabulate  #  Libreria para imprimir salidas de datos en forma de tabla 
Import shutil # Librería para copiar y remover archivos

class Productos:  # Clase Prodcutos
    def __init__(self): # Constructor de la clase Productos
        pass # Inicializa el objeto de la clase Productos

    def listarProducto(self) -> bool: # Metodo para listar los productos registrados
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("productos.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                rows = [] # Create an empty list to hold the rows
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    rows.append(row) # Append del row hacia la lista
                print('LISTA DE PRODUCTOS')  #  imprime el titulo de la lista
                print(tabulate(rows, headers='keys', tablefmt='fancy_grid')) # imprime los datos del registro como una lista de diccionarios con la libreria tabulate
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    
    def insertarProducto(self, sku: str, nombre: str, unidad: str)-> bool: # Metodo para insertar un producto
      try: # Prueba el codigo y si ocurre una Excepcion la atrapa
        with open("despensa.csv","a") as file: # abre el archivo en modo append
          while True: # bucle que pedira la entrada de datos sin fin
                sku = input("Escribe SKU: ") # pide el sku del producto
                nombre = input("Escribe nombre: ") # pide el nombre del producto
                unidad = input("Escribe unidad: ") # escriba la unidad de venta del producto
                file.write(f"{sku},{nombre},{unidad}\n") # escribe en el archivo los datos capturados, separamdolor por coma y en ese orden
      except Exception as e: # Atrapa cualquier excepcion
        print(f"Error :{e.args}") # Muestra en consola el error que ocurrio
      return False  # Regresa False si ocurrio un error en el metodo

    def buscarProducto(self, sku:str)-> bool: # Metodo para buscar un producto 
      try: # Prueba el codigo y si ocurre una Excepcion la atrapa
        with open("despensa.csv", "r") as file: # abre el archivo en modo lectura
            print("B U S C A R  P R O D U C T O") # impresion para dar a conocer la funcion en la que estas
            sku = input("Escribe el sku del producto: ") # pide el sku del producto a buscar
            reader = csv.reader(file, delimiter = ",") # crea un objeto de tipo reader para leer los registros y separarlos por ,        
            for row in reader: # ciclo for para recorrer todos los productos
                column = row[0] # variable temporal que ira almacenando el valor de un sku, row[0] indica que solo recorrera la fila 0 del archivo
                if column == sku: # si la variable temporal es igual al sku buscado
                    print(row) # imprime la posicion donde se encontro el sku
      except Exception as e: # Atrapa cualquier excepcion
        print(f"Error :{e.args}") # Muestra en consola el error que ocurrio
      return False  # Regresa False si ocurrio un error en el metodo

    def borrarProducto(self, sku: str) -> bool: # Metodo para borrar un producto
         try:  #  Prueba el codigo y si ocurre una Excepcion la atrapa
            with open('productos.csv', 'r') as entrada: # Abre el archivo para tener acceso a los registros
                reader = csv.reader(entrada)  #  lee el archivo abierto como un archivo csv y asinga una variable con la cual podemos iterar cada fila del archivo
             if encontrado: # Si se encontró el SKU, se imprime un mensaje de éxito y se devuelve True
                print(f'El producto con SKU {sku} ha sido borrado del archivo.') # mensaje de confirmacion
                return True # Devuelve True si la duncion se ejecuto correctamente

               filas = list(reader) #  convierte el objeto csv.reader en una lista en la cual cada line interna representa una fila del archivo csv
                sku = str(input('Teclea el sku a eliminar:'))  #  solicita al usuario que ingrese el SKU del producto que desea eliminar. 
            with open('productos.csv', 'w', newline='') as salida:  #  abre el archivo para escritura
                writer = csv.writer(salida)  #  crea un objeto csv.writer que permite escribir en un archivo CSV. 
                for fila in filas:  #  itera por cada fila del archivo
                    if fila[0] != sku:  #  Condicion que compara el sku
                        writer.writerow(fila)  # Si el SKU no coincide con el que se quiere eliminar, se escribe la fila en el archivo de salida
                    else:  #  Else que se ejecuta si la condicion if anterior es falsa
                        encontrado = True  #  se crea la variable encontrado y se le asigna el valor TRUE
        except Exception as e:  # Atrapa cualquier excepcion
            print(f"Error sku no encontrado :{e.args}")  # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def actualizarProducto(self, sku: str, nombre: str, unidad: str) -> bool: # Metodo para actualizar un producto
        try:
            with open("productos.csv", "r") as file: # Abre el archivo en modo lectura.
                productos = list(csv.DictReader(file)) # convierte el contenido del archivo en una lista de diccionarios.
            actualizacion = False # Regresa false
            sku = str(input('Ingresa el sku del producto a modificar: '))# Pregunta el sku del producto.
            for producto in productos:# recorre cada registro en el archivo
                if producto["sku"] == sku: # Compara el sku con el introducido.
                    print("Valores que podrían actualizarse del producto:")# Mensaje de que se puede actualizar.
                    print(f"Nombre: {producto['nombre']}, Unidad: {producto['unidad']}")# Nos  da los valores que se pueden actualizar
                    nombre = input("Ingrese el nuevo nombre del producto: ")# Pregunta el nuevo nombre.
                    unidad = input("Ingrese la nueva unidad del producto: ")# Pregunta la nueva unidad.
                    producto['nombre'] = nombre # Almacena el nuevo nombre
                    producto['unidad'] = unidad # Almacena la nueva unidad
                    actualizacion = True# Regresa true
                    print(f"Producto con el SKU {sku} se ha actualizado de manera correcta")# imprime confirmación.
                    break # Rompe

            if actualizacion: #si la actualizacion es true.
                with open("productos_temp.csv", "w", newline="") as file:# Abre el archivo en escritura.
                    writer = csv.DictWriter(file, fieldnames=["sku", "nombre", "unidad"]) # Se especifica que el archivo tendrá tres campos.
                    writer.writeheader() #  Escribe una fila en el archivo CSV que contiene los nombres de los campos definidos
                    writer.writerows(productos) # Escribe todas las filas de datos en el archivo

                shutil.move("productos_temp.csv", "productos.csv") # Mueve del archivo temporal al original.
                print("Registro actualizado correctamente.") # Imprime confirmacion 
                return True # Retorna true
            else: # si es false
                print(f"No se encontró ningún producto con el SKU {sku}") # imprime mensaje de que no se encontro.
                return False # Retorna false

        except Exception as e: # Atrapa cualquier execepcion
            print(f"Error: {e.args}") # imprime el error
            return False # retorna false
