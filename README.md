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


Comentarios sobre la implementación

Para el módulo de catálogo de productos, se requirió realizar los siguientes pasos. Primero, se creó una lista vacía para almacenar los productos. Luego, se implementó un menú para agregar productos, que mejoró las opciones de agregar películas, series, documentales, eventos deportivos en vivo y regresar al menú anterior. Se implementó una estructura condicional "if" para determinar qué función llamar dependiendo de la opción seleccionada por el usuario. Por ejemplo, si se elige la opción uno, se llama a la función "agregar_pelicula", y así sucesivamente.

En la función de agregar películas (y en las funciones correspondientes a otros tipos de productos), se solicitó al usuario ingresar el título, actor principal, director, año, costo de renta y costo de venta del producto. Estos valores se agregaron a la lista del catálogo, que fue creada anteriormente como una lista vacía.

Para la función de eliminar producto, se solicitó al usuario ingresar el título del producto que deseaba eliminar. Se sacó un bucle "for" para iterar sobre los productos en el catálogo y, si el título coincidía, se eliminó el producto de la lista.

En cuanto al módulo de mostrar productos, se implementó un bucle "while true" para mostrar el catálogo repetidamente hasta que se ingrese una opción válida para regresar al menú anterior. Utilizando estructuras condicionales "if", se llamaron a las funciones correspondientes para mostrar películas, series, documentales, etc. Se obtuvo un bucle "for" para iterar sobre los productos en cada categoría y mostrar sus títulos. Si no se encontraron productos en una categoría específica, se mostró un mensaje indicando que el catálogo estaba vacío.

Se realizó una actualización en la estructura del código para abordar las siguientes cuestiones. En primer lugar similar, se resolvió el problema relacionado con las películas y las series, ya que comparten características, como el "actor principal". En el módulo correspondiente, se implementó una condición para verificar si el tipo de producto es una película o una serie. En caso afirmativo, se imprimió el "actor principal" utilizando la sintaxis "producto.actor_principal". Si no se encontró ningún valor para el "actor principal" en el objeto producto, se mostró el mensaje "No hay actor principal".

De manera similar, se aplicó el enfoque mencionado anteriormente para el atributo "director". dependiendo del tipo de producto (película, serie o documental), se imprimió el "director" correspondiente utilizando la sintaxis "producto.director". En caso de que no se encuentre ningún valor para el "director", se mostró el mensaje "No hay director".

En relación a la búsqueda de productos, se solicitó al usuario ingresar una palabra clave y se creó una lista vacía llamada "resultados". A continuación, se implementó un bucle "for" para iterar sobre todos los productos en el catálogo. Se convirtió la palabra clave y el título de cada producto a minúsculas para facilitar la comparación. Si se encontró una coincidencia, se agregó el producto a la lista de resultados.

Posteriormente, se produjo una estructura condicional "si" para determinar si se encontraron resultados. En caso afirmativo, se imprimió el número de resultados encontrados. Luego, se inició otro bucle "for" para imprimir los detalles de cada producto en la lista de resultados.

En resumen, se llevaron a cabo las siguientes acciones: ajuste en la impresión del "actor principal" y el "director" según el tipo de producto, solicitud de una palabra clave para la búsqueda de productos, iteración sobre el catálogo y agregado de productos que coinciden con una lista de resultados, y finalmente, impresión de los detalles de cada producto encontrado.
Documentación: 

El código se organiza en cuatro módulos principales, y el punto de partida es el archivo "catalogo.py", ya que es desde allí que se inicia todo el proceso. Para comenzar, se presenta un menú que permite agregar productos, ya sean películas, series, documentales, eventos deportivos o regresar al menú anterior. Luego, se presentan las opciones numéricas correspondientes a cada tipo de producto, como 1 para películas, 2 para series, y así sucesivamente hasta el 4.

A continuación, se abordan los módulos de eliminación y agregado de productos. Se procede primero con la eliminación, donde se llama a la función "eliminar_producto". Dentro de esta función, se utiliza un ciclo "for" para iterar sobre cada producto en el catálogo. Si el título del producto coincide con el valor buscado, se retira del catálogo; de lo contrario, no se realiza ninguna acción. Posteriormente, se pasa al menú de agregado, donde nuevamente se imprimen los números correspondientes a las opciones disponibles para que el usuario elija. dependiendo de la elección del usuario, se llama una función específica. Por ejemplo, si se utiliza el número uno, se llama a la función "agregar_pelicula". A continuación, se solicitan todos los datos necesarios, como título, actor principal, director, año, costo de renta y venta, y se guarda la información en una lista creada en el archivo "catalogo.py". Este proceso se repite para cada tipo de producto.

Posteriormente, se aborda el módulo de "mostrar" y "búsqueda". Se importa el catálogo y se crea una nueva función llamada "mostrar_catalogo", que inicia un bucle infinito hasta que se ingresa una opción correcta. Al igual que en los anteriores, dependiendo de la opción elegida por el usuario, el programa realiza acciones específicas. Por ejemplo, si la opción es 3, se mostrarán los documentales llamando a la función correspondiente. Dentro de esta función, se utiliza un ciclo "for" para iterar sobre los documentales en el catálogo y, en caso de que haya documentales disponibles, se imprimen todos los títulos correspondientes. Si no hay documentos en el catálogo, se imprimirá un mensaje indicando esta situación. Para mostrar todos los productos en el catálogo, simplemente se imprime toda la lista.

Además, se ha creado una función llamada "print_producto" donde se imprimen los valores correspondientes al tipo y título del producto. Además, verifique los detalles adicionales de las especificaciones de cada tipo de producto. Por ejemplo, si el tipo es "Película" o "Serie", se imprime el actor principal; si el tipo es "Película", "Serie" o "Documental", se imprime el director; si el tipo es "Serie", se imprime el número de temporadas; si el tipo es "Documental", se imprime el tema. Si el tipo de producto es "Evento deportivo en vivo", se imprimen detalles como el deporte, fecha, hora y lugar del evento. Por último, se imprimen el costo de renta y el costo de venta del producto. Si alguno de estos valores no está presente en el diccionario del producto,

Finalmente, se encuentra el archivo "main.py", donde se importan todos los módulos.


NOTA: EL CORRESPONDIENTE DIAGRAMA DE BLOQUE SE ENCUENTRA EN EL ARCHIVO CO N EL NOMBRE "diagrama"
