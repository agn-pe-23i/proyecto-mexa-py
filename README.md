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

   - Para el modulo main: 
este código implementa un menú interactivo que permite al usuario realizar diferentes acciones en relación con un catálogo de productos. Las acciones incluyen agregar, buscar, eliminar, mostrar, cargar y guardar productos en el catálogo. El programa se ejecuta hasta que el usuario selecciona la opción de salida
e importan los módulos "catalogo" y "archivo". Esto implica que el programa hará uso de las funciones y variables definidas en dichos módulos.

A continuación, se define la función menu_principal(). Esta función muestra un menú principal en la consola con varias opciones, como agregar un producto, buscar un producto, eliminar un producto, mostrar el catálogo, cargar catálogo, guardar catálogo y salir. Luego, solicite al usuario que seleccione una opción y devuelva la opción seleccionada.

La función ejecutar_opcion(opcion)se encarga de ejecutar la acción correspondiente según la opción seleccionada por el usuario. Utilice una serie de declaraciones if-elif-elsepara determinar qué acción tomar en función de la opción seleccionada. Por ejemplo, si la opción es "1", se llama a la función catalogo.menu_agregar()del módulo "catalogo".

La función main()es el punto de entrada principal del programa. En un bucle infinito while True, obtiene la opción seleccionada del menú principal utilizando la función menu_principal(). Luego, verifica si la opción es "7" (Salir). Si es así, se rompe el bucle y el programa finaliza. Si no es la opción de salida, se llama a la función ejecutar_opcion(opcion)para ejecutar la acción correspondiente.

La línea if __name__ == "__main__":verifica si el programa se está ejecutando directamente (no se importa como un módulo en otro programa). Si es así, se llama a la función main()para comenzar la ejecución del programa.8


  -Para el modulo catalogo: 




Documentación: 

El código se organiza en cuatro módulos principales, y el punto de partida es el archivo "catalogo.py", ya que es desde allí que se inicia todo el proceso. Para comenzar, se presenta un menú que permite agregar productos, ya sean películas, series, documentales, eventos deportivos o regresar al menú anterior. Luego, se presentan las opciones numéricas correspondientes a cada tipo de producto, como 1 para películas, 2 para series, y así sucesivamente hasta el 4.

A continuación, se abordan los módulos de eliminación y agregado de productos. Se procede primero con la eliminación, donde se llama a la función "eliminar_producto". Dentro de esta función, se utiliza un ciclo "for" para iterar sobre cada producto en el catálogo. Si el título del producto coincide con el valor buscado, se retira del catálogo; de lo contrario, no se realiza ninguna acción. Posteriormente, se pasa al menú de agregado, donde nuevamente se imprimen los números correspondientes a las opciones disponibles para que el usuario elija. dependiendo de la elección del usuario, se llama una función específica. Por ejemplo, si se utiliza el número uno, se llama a la función "agregar_pelicula". A continuación, se solicitan todos los datos necesarios, como título, actor principal, director, año, costo de renta y venta, y se guarda la información en una lista creada en el archivo "catalogo.py". Este proceso se repite para cada tipo de producto.

Posteriormente, se aborda el módulo de "mostrar" y "búsqueda". Se importa el catálogo y se crea una nueva función llamada "mostrar_catalogo", que inicia un bucle infinito hasta que se ingresa una opción correcta. Al igual que en los anteriores, dependiendo de la opción elegida por el usuario, el programa realiza acciones específicas. Por ejemplo, si la opción es 3, se mostrarán los documentales llamando a la función correspondiente. Dentro de esta función, se utiliza un ciclo "for" para iterar sobre los documentales en el catálogo y, en caso de que haya documentales disponibles, se imprimen todos los títulos correspondientes. Si no hay documentos en el catálogo, se imprimirá un mensaje indicando esta situación. Para mostrar todos los productos en el catálogo, simplemente se imprime toda la lista.

Además, se ha creado una función llamada "print_producto" donde se imprimen los valores correspondientes al tipo y título del producto. Además, verifique los detalles adicionales de las especificaciones de cada tipo de producto. Por ejemplo, si el tipo es "Película" o "Serie", se imprime el actor principal; si el tipo es "Película", "Serie" o "Documental", se imprime el director; si el tipo es "Serie", se imprime el número de temporadas; si el tipo es "Documental", se imprime el tema. Si el tipo de producto es "Evento deportivo en vivo", se imprimen detalles como el deporte, fecha, hora y lugar del evento. Por último, se imprimen el costo de renta y el costo de venta del producto. Si alguno de estos valores no está presente en el diccionario del producto,

Finalmente, se encuentra el archivo "main.py", donde se importan todos los módulos.


NOTA: EL CORRESPONDIENTE DIAGRAMA DE BLOQUE SE ENCUENTRA EN EL ARCHIVO CO N EL NOMBRE "diagrama"
