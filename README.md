[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
***************************
 profesor: Abel García Nájera 

Integrantes del equipo y sus matriculas: 
   - Diego Dominic Reyes Pastrana 2223068828
   - Rosas Navarrete Erick 2223028628
   - Sánchez Ortiz Estefany Harisvet 2213028278 

PROYECTO FINAL de Programación Estructurada 

***************************

Introducción:

El presente trabajo tiene como objetivo desarrollar un diseño top-down para el desarrollo de un programa que cumpla con los requisitos de un servicio de streaming en particular. Para lograr esto, se utilizarán diferentes conceptos y temas estudiados en la Unidad de Enseñanza-Aprendizaje (UEA) correspondiente, tales como estructuras de control, tipos de datos, secuencias de datos, funciones, módulos, registros y archivos.

El diseño propuesto se basa en la creación de un programa principal que interactúa con un catálogo de productos, el cual contiene una amplia variedad de películas, series, documentales y eventos deportivos en vivo. Para manipular correctamente este catálogo y asegurar una experiencia de usuario fluida, se implementarán diversas estructuras de control que permitirán la navegación y selección de productos de manera intuitiva a través de una serie de menús.

Además, se hará uso de los diferentes tipos de datos disponibles para almacenar y organizar la información relevante de cada producto en el catálogo. Se implementarán funciones y módulos para facilitar la modularidad y reutilización de código, asegurando así un desarrollo eficiente y escalable.


Comentarios sobre la implementación: 

El código se organiza en cuatro módulos principales, y el punto de partida es el archivo "catalogo.py", ya que es desde allí que se inicia todo el proceso. Para comenzar, se presenta un menú que permite agregar productos, ya sean películas, series, documentales, eventos deportivos o regresar al menú anterior. Luego, se presentan las opciones numéricas correspondientes a cada tipo de producto, como 1 para películas, 2 para series, y así sucesivamente hasta el 4.

A continuación, se abordan los módulos de eliminación y agregado de productos. Se procede primero con la eliminación, donde se llama a la función "eliminar_producto". Dentro de esta función, se utiliza un ciclo "for" para iterar sobre cada producto en el catálogo. Si el título del producto coincide con el valor buscado, se retira del catálogo; de lo contrario, no se realiza ninguna acción. Posteriormente, se pasa al menú de agregado, donde nuevamente se imprimen los números correspondientes a las opciones disponibles para que el usuario elija. dependiendo de la elección del usuario, se llama una función específica. Por ejemplo, si se utiliza el número uno, se llama a la función "agregar_pelicula". A continuación, se solicitan todos los datos necesarios, como título, actor principal, director, año, costo de renta y venta, y se guarda la información en una lista creada en el archivo "catalogo.py". Este proceso se repite para cada tipo de producto.

Posteriormente, se aborda el módulo de "mostrar" y "búsqueda". Se importa el catálogo y se crea una nueva función llamada "mostrar_catalogo", que inicia un bucle infinito hasta que se ingresa una opción correcta. Al igual que en los anteriores, dependiendo de la opción elegida por el usuario, el programa realiza acciones específicas. Por ejemplo, si la opción es 3, se mostrarán los documentales llamando a la función correspondiente. Dentro de esta función, se utiliza un ciclo "for" para iterar sobre los documentales en el catálogo y, en caso de que haya documentales disponibles, se imprimen todos los títulos correspondientes. Si no hay documentos en el catálogo, se imprimirá un mensaje indicando esta situación. Para mostrar todos los productos en el catálogo, simplemente se imprime toda la lista.

Además, se ha creado una función llamada "print_producto" donde se imprimen los valores correspondientes al tipo y título del producto. Además, verifique los detalles adicionales de las especificaciones de cada tipo de producto. Por ejemplo, si el tipo es "Película" o "Serie", se imprime el actor principal; si el tipo es "Película", "Serie" o "Documental", se imprime el director; si el tipo es "Serie", se imprime el número de temporadas; si el tipo es "Documental", se imprime el tema. Si el tipo de producto es "Evento deportivo en vivo", se imprimen detalles como el deporte, fecha, hora y lugar del evento. Por último, se imprimen el costo de renta y el costo de venta del producto. Si alguno de estos valores no está presente en el diccionario del producto,

Finalmente, se encuentra el archivo "main.py", donde se importan todos los módulos.

  



Documentación: 


    - Para el modulo main:

este código implementa un menú interactivo que permite al usuario realizar diferentes acciones en relación con un catálogo de productos. Las acciones incluyen agregar, buscar, eliminar, mostrar, cargar y guardar productos en el catálogo. El programa se ejecuta hasta que el usuario selecciona la opción de salida
e importan los módulos "catalogo" y "archivo". Esto implica que el programa hará uso de las funciones y variables definidas en dichos módulos.

A continuación, se define la función menu_principal(). Esta función muestra un menú principal en la consola con varias opciones, como agregar un producto, buscar un producto, eliminar un producto, mostrar el catálogo, cargar catálogo, guardar catálogo y salir. Luego, solicite al usuario que seleccione una opción y devuelva la opción seleccionada.

La función ejecutar_opcion(opcion) se encarga de ejecutar la acción correspondiente según la opción seleccionada por el usuario. Utilice una serie de declaraciones if-elif-elsepara determinar qué acción tomar en función de la opción seleccionada. Por ejemplo, si la opción es "1", se llama a la función catalogo.menu_agregar() del módulo "catalogo".

La función main()es el punto de entrada principal del programa. En un bucle infinito while True, obtiene la opción seleccionada del menú principal utilizando la función menu_principal(). Luego, verifica si la opción es "7" (Salir). Si es así, se rompe el bucle y el programa finaliza. Si no es la opción de salida, se llama a la función ejecutar_opcion(opcion) para ejecutar la acción correspondiente.

La línea if __name__ == "__main__": verifica si el programa se está ejecutando directamente (no se importa como un módulo en otro programa). Si es así, se llama a la función main() para comenzar la ejecución del programa.


    - Para el modulo catalogo: 

Este modulo implementa varias funciones relacionadas con la manipulación de un catálogo de productos. 
agregar_producto(): Esta función muestra un menú de opciones para agregar un producto al catálogo. dependiendo de la opción seleccionada por el usuario, se llama a la función correspondiente para agregar una película, serie, documental o evento deportivo.

menu_agregar(): Esta función es similar a agregar_producto(), pero se utiliza específicamente cuando se llama desde la opción "Agregar un producto" en el menú principal. Muestra el mismo menú de opciones y realiza la misma lógica de redireccionamiento a las funciones correspondientes según la opción seleccionada.

mostrar_catalogo(): Esta función muestra un menú de opciones para mostrar diferentes categorías de productos del catálogo. además de la opción seleccionada, se llama a las funciones correspondientes para mostrar películas, series, documentales, eventos deportivos o el catálogo completo.

eliminar_producto(): Esta función solicita al usuario que ingrese el título de un producto y busca en el catálogo si existe un producto con ese título. Si se encuentra, se elimina del catálogo. Si no se encuentra, se muestra un mensaje que indica que no se encontró el producto.

Las funciones agregar_pelicula(), agregar_serie(), agregar_documental() y agregar_evento_deportivo(): Estas funciones se llaman desde las funciones agregar_producto()o menu_agregar()según la opción seleccionada por el usuario. Solicitan al usuario información específica sobre cada tipo de producto y luego agregan el producto al catálogo con los datos proporcionados.

Las funciones mostrar_peliculas(), mostrar_series(), mostrar_documentales(), mostrar_eventos_deportivos() y mostrar_todo(): Estas funciones se llaman desde la función mostrar_catalogo() según la opción seleccionada por el usuario. Cada función registra el catálogo y muestra los productos correspondientes a la categoría seleccionada.

print_producto(): Esta función auxiliar recibe un diccionario que representa un producto y muestra su información formateada en la consola.

buscar_producto(): Esta función solicita al usuario que ingrese una palabra clave y busque en el catálogo todos los productos cuyo título contenga dicha palabra clave (ignorando mayúsculas y minúsculas). Luego muestra los productos encontrados.



    - Para el modulo Archivo: 

import catalogo: Esta línea importa un módulo o archivo llamado "catalogo" en el cual se encuentren definidas funciones relacionadas con el catálogo de productos.

def cargar_catalogo(): Aquí se define una función llamada "cargar_catalogo()" que se encargará de cargar el catálogo desde un archivo de texto.

nombre_archivo = input("Ingrese el nombre del archivo: "): Esta línea solicita al usuario que ingrese el nombre del archivo de texto que contiene el catálogo. El valor ingresado se guarda en la variable "nombre_archivo".

try: Se inicia un bloque de código donde se manejarán las excepciones que pueden ocurrir durante la ejecución.

with open(nombre_archivo, "r") as archivo: Se utiliza la declaración "with open" para abrir el archivo especificado en modo de lectura ("r"). El archivo se asocia a la variable "archivo" dentro del bloque de código.

catalogo.catalogo_productos = eval(archivo.read()): Aquí se lee el contenido del archivo utilizando el método "read()" y se utiliza la función "eval()" para evaluar la cadena de texto leído como si fuera un código de Python. Se espera que el contenido del archivo represente un diccionario o estructura de datos que se autorizará a la variable "catalogo_productos" del módulo "catalogo".

print("El catálogo se ha cargado."): Se imprime un mensaje indicando que el catálogo ha sido cargado correctamente.

except FileNotFoundError:: Si ocurre un error del tipo "FileNotFoundError", significa que el archivo especificado no existe y se ejecutará este bloque de código. Se imprime un mensaje indicando que el catálogo no existe.

except:: Este bloque de código se ejecutará si ocurre cualquier otro tipo de excepción no capturado anteriormente. Se imprime un mensaje indicando que ha ocurrido un error genérico.

def guardar_catalogo():: Se define otra función llamada "guardar_catalogo()" que se encargará de guardar el catálogo en un archivo de texto.

nombre_archivo = input("Ingrese el nombre del archivo: "): Similar a la línea 3, se solicita al usuario que ingrese el nombre del archivo en el que se guardará el catálogo.

try:: Se inicia otro bloque "try" para manejar las excepciones.

with open(nombre_archivo, "w") as archivo:: Se utiliza "with open" para abrir el archivo en modo de escritura ("w"). El archivo se asocia a la variable "archivo" dentro del bloque.

archivo.write(str(catalogo.catalogo_productos)): Se escribe en el archivo el contenido de la variable "catalogo_productos" convertido a una cadena de texto utilizando la función "str()".

print("Se ha guardado correctamente."): Se imprime un mensaje indicando que el catálogo se ha guardado correctamente.

except:: Si ocurre alguna excepción durante el proceso de guardado, se ejecutará este bloque de código. Se imprime un mensaje indicando que ha ocurrido un error genérico




Para poder hacer uso de los modulos y del programa se deben seguir los siguientes pasos: 

El primer paso a seguir es abrir el repositorio en GitHub para poder visualizar los módulos y toda la información necesaria de su uso. Una vez abierto GitHub, se deben descargar los 3 módulos correspondientes, los cuales son "catalogo.py", "archivo.py" y "main.py". Además, se debe descargar el archivo de texto donde se encuentra cargado ya un catálogo predeterminado, el cual lleva por nombre "Push1.txt". El orden de las descargas no tiene ninguna importancia, sin embargo, todos los archivos descargados deben contenerse en una carpeta nueva y vacía, es decir, que solo contenga los archivos de este programa.

Una vez tengamos la carpeta lista, podemos seleccionarla y dar un clic derecho para poder elegir la opción "ABRIR CON". En este caso, el programa se ejecutará en PyCharm o, en su defecto, en la terminal.

Y asi estara listo el codigo para poder usar. Se posiciona en el código del módulo main y solo ejecutamos.

NOTA: En caso de que el archivo de texto donde se encuentra almacenado el catálogo predeterminado tenga un nombre diferente, solo se debe hacer un ajuste al nombre del mismo archivo, es decir, renombrar dicho archivo, y así podrá cargar exitosamente el archivo .txt del catálogo.



Diagrama de estructura: 

![WhatsApp Image 2023-06-21 at 21 07 33](https://github.com/agn-pe-23i/proyecto-mexa-py/assets/125591740/3eff9c61-9e1b-433d-be1b-40446b635f87)


En el diagrama de estructura presentado hace referencia a dos módulos: "catálogo" y "archivo", los cuales son desplegados desde el módulo principal llamado "main". A continuación, se detallan las funciones y operaciones que cada uno de estos módulos realiza:

Módulo "catálogo":

Eliminar producto: Esta función requiere un dato de entrada de tipo string (el nombre o identificador del producto a eliminar) y devuelve un dato de salida de tipo string (un mensaje de confirmación).
Agregar producto: Esta función necesita un dato de entrada de tipo string (los detalles del producto a agregar) y devuelve un dato de salida de tipo string (por ejemplo, un mensaje de confirmación o el identificador asignado al producto).
Buscar producto: Esta función toma un dato de entrada de tipo string (un criterio de búsqueda, como el nombre del producto) y devuelve un dato de salida de tipo string (posiblemente los detalles del producto encontrado).
Mostrar catálogo: Esta función requiere un dato de entrada de tipo entero (alguna opción o parámetro) y devuelve un dato de salida de tipo string (el catálogo completo en forma de texto).

Módulo "archivo":

Guardar catálogo: Esta función necesita un dato de entrada de tipo string (probablemente el nombre o ubicación del archivo) y devuelve un dato de salida de tipo string (por ejemplo, un mensaje de confirmación o el estado del guardado).
Cargar catálogo: Esta función requiere un dato de entrada de tipo string (el nombre del archivo a cargar) y devuelve un dato de salida de tipo string (por ejemplo, un mensaje de confirmación o el estado de la carga).
En resumen, el módulo "catálogo" se encarga de operaciones relacionadas con la manipulación y visualización de productos en el catálogo, como agregar, eliminar, buscar y mostrar productos. Por otro lado, el módulo "archivo" se ocupa de las operaciones de guardar y cargar el catálogo en un archivo.

