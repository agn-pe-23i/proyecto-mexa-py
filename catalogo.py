#Hacemos una lista vacia para el catalogo
catalogo_productos = []
#Llamamos una funcion para el menu cuando se requiera guardar un producto
def agregar_producto():
    print("Menú agregar producto")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Evento deportivo en vivo")
    print("5. Regresar")

    opcion = int(input("Seleccione una opción: "))
#Aqui llamamos a las funciones dependiendo que haya metido el usuario
    if opcion == 1:
        agregar_pelicula()
    elif opcion == 2:
        agregar_serie()
    elif opcion == 3:
        agregar_documental()
    elif opcion == 4:
        agregar_evento_deportivo()
