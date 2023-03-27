import csv  # Librería para abrir, leer y escribir archivos CSV


class Tiendas:  # Clase Tiendas
    def __init__(self):  # Construcctor de la clase Tiendas
        pass  # Inicializa el objeto Tiendas

    def listarTiendas(self) -> bool: # Metodo para listar los productos registrados
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("tiendas.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(row) # imprime los datos del registro como un diccionario
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def insertarTienda(self) -> bool:  # Metodo para insertar una tienda
        try:
            with open("tiendas.csv", mode='a', newline='') as file: # Abre el archivo para poder registar.
               campos = ["id", "nombre", "coordenadas", "direccion"] #  Se define la lista con los nombres de los campos del archivo CSV.
               writer = csv.DictWriter(file, fieldnames=campos, delimiter=";")# Se define un objeto y el delimitador a utilizar 
               id = input("Ingrese el ID de la tienda: ")# Se pide ingresar un ID.
               nombre = input("Ingrese el nombre de la tienda: ")# Se pide ingresar un nombre.
               coordenadas = input("Ingrese coordenadas de la tienda: ")# Se pide ingrsar las cooerdenadas.
               direccion = input("Ingrese la dirección de la tienda: ")# Se pide ingresAR la direccion.
               if id and nombre and direccion and coordenadas:# Se verifica que los campos requeridos no estén vacíos.
                   writer.writerow({"id": id, "nombre": nombre,"coordenadas": coordenadas, "direccion": direccion})# Se escribe una nueva fila con los valores.
                   print(f"Se ingreso de manera correcta la tienda con nombre {nombre} ")# Se imprime confirmacion
                   return True# regres True si se ejecuto de manera correcta.
               else:
                   print("No se registró de manera correcta.")# Imprime advertencia.
        except Exception as e:# # Atrapa cualquier excepcion.
          print(f"Error al insertar la tienda: {e}")#  # Muestra en consola el error que ocurrio.
        return False  # Regresa False si ocurrio un error en el metodo

    def buscarTienda(self, nombre: str) -> bool:  # Metodo para buscar tiendas por nombre
        try: #  Prueba el codigo y si ocurre una Excepcion la atrapa
         for tienda in tiendas.csv: #busca el archivo de tiendas
             if tienda.nombre == nombre:
              return True #Si encuentra alguna coincidencia regresa TRUE
               return False  # Regresa False si ocurrio un error en el metodo
    
    def borrarTienda(self, id: str) -> bool: # Metodo para borrar una
         try:  #  Prueba el codigo y si ocurre una Excepcion la atrapa
            with open('tiendas.csv', 'r') as entrada: # Abre el archivo para tener acceso a los registros
                reader = csv.reader(entrada)  #  lee el archivo abierto como un archivo csv y asinga una variable con la cual podemos iterar cada fila del archivo
                filas = list(reader) #  convierte el objeto csv.reader en una lista en la cual cada line interna representa una fila del archivo csv
                id = str(input('Ingresa el ID de la tienda a eliminar:'))  #  solicita al usuario que ingrese el ID de la tienda que desea eliminar. 
            with open('tiendas.csv', 'w', newline='') as salida:  #  abre el archivo para escritura
                writer = csv.writer(salida)  #  crea un objeto csv.writer que permite escribir en un archivo CSV. 
                for fila in filas:  #  itera por cada fila del archivo
                    if fila[0] != tienda:  #  Condicion que compara el id
                        writer.writerow(fila)  # Si el ID no coincide con el que se quiere eliminar, se escribe la fila en el archivo de salida
                    else:  #  Else que se ejecuta si la condicion if anterior es falsa
                        encontrado = True  #  se crea la variable encontrado y se le asigna el valor TRUE
            if encontrado: # Si se encontró el ID, se imprime un mensaje de éxito y se devuelve True
                print(f'La tienda con el ID {id} ha sido borrado de manera correcta.') # mensaje de confirmacion
                return True # Devuelve True si la duncion se ejecuto correctamente

        except Exception as e:  # Atrapa cualquier excepcion
            print(f"Error ID no encontrado :{e.args}")  # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
    
    def actualizarTienda(self) -> bool:  # Metodo para actualizar los datos de un tienda
          for tienda in self.lista_tiendas: 
              if tienda.nombre == nombre: #Permite actualizar algun dato
               tienda.actualizar(nuevos_datos) #Se agregan los datos nuevos
               return True #Si la actualizacion de datos fue exitosa regresa un TRUE
            return False  # Regresa False si ocurrio un error en el metodo
