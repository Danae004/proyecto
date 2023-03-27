# Proyecto para llevar el control de la compra de despensa y variación de precios.

## 0. Versión de la plantilla

Plantilla inicial versión 0.06032023.8

## 1. Introducción

La compra de productos es una de las actividades mas recurrentes hoy en día. La cantidad de tiendas que ofrecen los mismos productos
es amplia y a la vez que mas tiendas se vuelven de la preferencia del público, se crea la competencia económica. Muchos son los 
fatores por los que una persona decide comprar en determinada tienda, ya sea por su ubicación, precios, familiaridad u otras. Es por
eso que creemos necesario la implementación de una estrategia para que todos esos factores sean comparados y al final, el cliente
pueda tener una mejor desición en cuanto a sus compras.

## 2. Objetivos

✦ Implementar un sistema de seguimiento de los precios de los productos para detectar las variaciones en los mismos y tomar decisiones informadas al momento de realizar la compra.

✦ Realizar mejoras continuas en el sistema para asegurar su eficacia a largo plazo

✦ Diseñar e implementar un sistema de seguimiento de precios para detectar variaciones en los precios de los productos y tomar medidas para minimizar el impacto en el presupuesto familiar

✦ Establecer un mecanismo de comparación de precios entre distintos establecimientos, para que el usuario pueda identificar las opciones más económicas para sus compras

✦ Generar reportes periódicos sobre el comportamiento de los precios de los productos adquiridos, para que el usuario pueda tomar decisiones informadas sobre cuándo y dónde comprar.

## 3. Integrantes
|matricula|nombre|
|--|--|
|1722110455| Oscar Adahir Garcia Sanchez|
|1722110547| Juan Carlos Hernandez Vazquez|
|1722110300| Said Isaac Leon Lara|
|1722110136| Citlali Hernandez Perez|
|1722110078| Josandy Danae Barqueras Andrade|

## 4. Herramientas de Desarrollo

|Herramienta|Concepto|
|--|--|
|Visual Studio Code| Es un editor de código eficaz y ligero con herramientas integradas para implementar código fácilmente|
|Replit| Es una plataforma gratuita para programar desde el navegador|
|Bloc de notas| Es un editor de texto incluido en los sistemas operativos de Microsoft desde 1985|
|Market Space| Es un espacio físico de colaboración abierta donde las personas tienen acceso a recursos, conocimiento, conexiones profesionales y herramientas que comparten para trabajar en sus proyectos|

## 5. Planeación de actividades y asignación de tareas

|No.|Función|Estado|Fecha programada|Fecha realizada|Responsable|Descripción|
|--|--|--|--|--|--|--|
|1|Archivo productos.csv|ToDo|NA|NA|Grupal|NA|
|2|Método listarProductos()|DONE|NA|18/03/2023|Carlos 1|Funcion que permite listar productos en una tabla|
|3|Método insertarProductos()|DONE|NA|16/03/2023|Said 1|Función que permite insertar nuevos productos a la BD|
|4|Método buscarProductos()|DONE|NA|16/03/2023|Said 2|Función que permite buscar productos según su SKU|
|5|Método borrarProductos()|DONE|NA|18/03/2023|Carlos 2|Funcion que permite eliminar productos de la base de datos|
|6|Método actualizarProductos()|ToDo|NA|NA|Oscar 1|NA|
|7|Llamar al método listarProductos() en menú|DONE|NA|19/03/2023|Carlos 3|Llamada al metodo listarProductos de la clase productos en el archivo main.py|
|8|Llamar al método insertarProductos() en menú|ToDo|NA|NA|Oscar 2|NA|
|9|Llamar al método buscarProductos() en menú|DONE|NA|17/03/2023|Said 3|Llamada al método buscarProductos() en el menú|
|10|Llamar al método borrarProductos() en menú|DONE|NA|17/03/23|Said 4|Llamada añ método borrarProductos() en el menú|
|11|Llamar al método actualizarProductos() en menú|ToDo|NA|20/03/2023|Citlali 1|Se llama al método actualizarProducto desde el menú|
|12|Archivo tiendas.csv|ToDo|NA|NA|Grupal|NA|
|13|Método listarTiendas()|ToDo|NA|NA|Josandy 1|Permite listar todas las tiendas agregadas|
|14|Método insertarTiendas()|ToDo|18/03/2023|20/03/2023|Oscar 3|Funcion que permite insertar una tienda|
|15|Método buscarTiendas()|ToDo|NA|20/03/28|Josandy 2|Permite buscar una tienda en particular para saber si forma o no parte de la base de datos|
|16|Método borrarTiendas()|ToDo|19/03/2023|19/03/2023|Oscar 4|Funcion que permite borrar una tienda|
|17|Método actualizarTiendas()|ToDo|NA|20/03/28|Josandy 3|Permite ingresar nuevas tiendas y actualizar los datos|
|18|Llamar al método listarTiendas() en menú|DONE|NA|21/03/2023|Carlos 4|Se llama al metodo listar tiendas en el menú, el cual permite acceder a el|
|19|Llamar al método insertarTiendas() en menú|ToDo|NA|NA|Josandy 4|Permite agregar nuevas tiendas a la base de datos|
|20|Llamar al método buscarTiendas() en menú|ToDo|NA|NA|Citlali 2|Se llama al método buscarTiendas en el menú|
|21|Llamar al método borrarTiendas() en menú|DONE|NA|21/03/2023|Carlos 5|Se llama al metodo borrar tiendas en el menú, el cual permite acceder a el|
|22|Llamar al método actualizarTiendas() en menú|ToDo|NA|20/03/2023|Citlali 3|Se llama al método actualizarTiendas en el menú|
|23|Archivo despensa.csv|ToDo|NA|NA|Grupal|NA|
|24|Método listarCompras()|ToDo|NA|NA|Said 5|NA|
|25|Método insertarCompra()|ToDo|NA|NA|Said 6|NA|
|26|Método buscarComprasFecha()|ToDo|NA|NA|Oscar 5|NA|
|27|Método borrarCompra()|ToDo|NA|NA|Carlos 6|NA|
|28|Método actualizarCompra()|ToDo|NA|20/03/2023|Citlali 4|Se crea un método para actualizar la despensa|
|29|Método valorMinimoProducto()|ToDo|NA|NA|Oscar 6|NA|
|30|Método valorMaximoProducto()|ToDo|NA|NA|Citlali 5|Se crea un método para saber cual es el valor maximo de un producto|
|31|Llamar al método listarCompras()|ToDo|NA|NA|Citlali 6|Se llama al método listarCompras|
|32|Llamar al método insertarCompra()|ToDo|NA|NA|Carlos 7|NA|
|33|Llamar al método buscarComprasFecha()|ToDo|NA|NA|Josandy 5|NA|
|34|Llamar al método borrarCompra()|ToDo|NA|NA|Citlali 7|NA|
|35|Llamar al método valorMinimoProducto()|ToDo|NA|NA|Josandy 6|NA|
|36|Llamar al método valorMaximoProducto()|ToDo|NA|NA|Carlos 8|NA|
|37|Completar el método menu() con los submenus necesarios|DONE|NA|20/03/2023|Carlos 9|Se creo un menu con submenus para acceder a las diferentes funciones|
|38|FUNCIÓN INNOVADORA PROPUESTA POR EL EQUIPO|ToDo|NA|NA|Grupal|NA|
|39|Capturar la Introducción|DONE|NA|17/03/2023|Said 7|Introducción al Proyecto|
|40|Capturar los Objetivos|ToDo|NA|20/03/2023|Citlali 8|Se describen los objetivos que quiere alcanzar el grupo con este proyecto|
|41|Capturar los Integrantes|ToDo||14/03/2023|Oscar 7|Se registro a los integrantes del equipo|
|42|Capturar las Herramientas de desarrollo|ToDo|NA|NA|Josandy 8|NA|
|43|Capturar las Conclusiones|ToDo|25/03/2023|Oscar 8|Se crea una conclusion sobre el proyecto|
|44|Capturar la Bibliografía|ToDo|NA|NA|Said 8|NA|
|45|Tabla de problemas y soluciones|ToDo|NA|NA|Grupal|NA|

## 6. Tabla de problemas y soluciones

|No|Identificación del problema|Causa|Alternativas de solución|Toma de decisión con argumento|
|--|--|--|--|--|
|1|Problema 1|Causa 1|Alternativa 1|Decisión 1|
|2|Desorganizacion|--|--|--|
|3|Desinteres|--|--|--|
|4|Falta de comunicacion|--|--|--|
|5|Diferentes soluciones para el mismo problema|--|--|--|
|6|Irresponsabilidad de integrantes del equipo|--|--|--|
|7|Falta de preparacion|--|--|--|
|8|Falta de motivacion|--|--|--|
|9|Falta de equipo|--|--|--|
|10|Actividades personales|--|--|--|
|11|Conectividad|--|--|--|
|12|No saber como hacer las cosas|--|--|--|
|13|No saber trabajar en equipo|--|--|--|
|14|Guardar datos vacios|--|--|--|
|15|


## 7. Conclusiones:

En conclusión, implementar un sistema de seguimiento de precios de productos es una estrategia efectiva para tomar decisiones informadas al momento de realizar compras y minimizar el impacto en el presupuesto familiar. Es importante realizar mejoras continuas en el sistema para asegurar su eficacia a largo plazo. Además, diseñar e implementar un mecanismo de comparación de precios entre distintos establecimientos, así como generar reportes periódicos sobre el comportamiento de los precios de los productos adquiridos, son acciones adicionales que pueden ser de gran ayuda para el usuario a la hora de tomar decisiones informadas sobre cuándo y dónde comprar. En resumen, un sistema de seguimiento de precios puede ser una herramienta útil y valiosa para ahorrar dinero en las compras y maximizar el valor de los productos adquiridos.

## 8. Bibliografía

1. [Python Documentation - CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
2. [Open Route Service](https://openrouteservice.org)

Agregar las referencias bibliográficas utilizadas

## 9. Reglas:

0. Realizar un fork al repositorio, crear un nuevo repositorio con los integrantes del equipo.
1. Las funciones deben ser asignadas entre los integrantes del equipo (Solamente se pueden asignar un máximo de 5 actividades grupales)
2. Todo el código debe estar documentado para ser considerado.
3. Las evaluaciones las realizará un solo integrante del equipo seleccionado al azar.
4. La útlima función del sistema será propuesta y desarrollada por el equipo, por ejemplo:
* La tienda más cercana a mi ubicación.
* La tienda en donde está más barato un producto.
* La tienda en donde está más barata la despensa completa.
* Análisis de Series de tiempo.
* Predicción del costo de un producto determinado.
5. El responsable de cada actividad tiene las siguientes tareas:
* Programar el algoritmo correspondiente.
* Documentar su código.
* Validar que su código funcione correctamente.
* Subir su código al repositorio grupal.
6. Responsabilidades del grupo:
* Seleccionar las tecnologías que van a ocupar.
* Repartir de forma equitativa las actividades del proyecto.
* Definir la función innovadora del proyecto.
* Definir la Introducción, Objetivos y Conclusiones.
* Designar un ecargado de capturar la Introduccion, Objetivos y Conclusiones.
* Identificar los problemas y soluciones durante el desarrollo del proyecto, para realizar las mejoras oportunas.
* Designar un encargado de capturar la tabla de problemas y soluciones.
7. Método para la gestión del flujo de trabajo empleando "KANBAN":
* ToDo - Tarea pendiente de realizarse.
* Doing - Tarea que se esta realizando.
* Done - Tarea terminada completamente
