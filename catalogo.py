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
#Aqui llamamos a las funciones dependiendo que haya metido el usuario empieza en la linea 81 y termina en la 119
    if opcion == 1:
        agregar_pelicula()
    elif opcion == 2:
        agregar_serie()
    elif opcion == 3:
        agregar_documental()
    elif opcion == 4:
        agregar_evento_deportivo()
#Hacemos un menu para agregar
def menu_agregar():
    print("Menú agregar producto")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Evento deportivo en vivo")
    print("5. Regresar")

    opcion = input("Seleccione una opción: ")
#Las funciones se llaman dependiendo que opcion haya seleccionado el usuario empiezan las finciones en la linea
    if opcion == "1":
        agregar_pelicula()
    elif opcion == "2":
        agregar_serie()
    elif opcion == "3":
        agregar_documental()
    elif opcion == "4":
        agregar_evento_deportivo()
    elif opcion == "5":
        return
    else:
        print("Seleccione una opcion valida.")
#Se agrega un menu para la opcion de agregar
def mostrar_catalogo():
    while True:
        print("Menú mostrar catálogo")
        print("1. Películas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos deportivos")
        print("5. Todo")
        print("6. Regresar")

        opcion = input("Por favor, haga una selección: ")
#Se llaman a las funciones dependiendo que haya seleccionado el usuario
        if opcion == "1":
            mostrar_peliculas()
        elif opcion == "2":
            mostrar_series()
        elif opcion == "3":
            mostrar_documentales()
        elif opcion == "4":
            mostrar_eventos_deportivos()
        elif opcion == "5":
            mostrar_todo()
        elif opcion == "6":
            return
        else:
            print("Seleccione una opción válida.")
def eliminar_producto():
    titulo = input("Ingrese el título del producto que desea eliminar: ")

    for producto in catalogo_productos:
        if producto["Título"] == titulo:
            catalogo_productos.remove(producto)
            print("El producto fue eliminado.")
            return

    print("No se encontró producto.")
#Hacemos varias funciones ya sea para agregar peliculas, series etc
def agregar_pelicula():
    titulo = input("Ingrese el título de la película: ")
    actor_principal = input("Ingrese el actor principal de la película: ")
    director = input("Ingrese el director de la película: ")
    anio = input("Ingrese el año de la película: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    catalogo_productos.append({"Tipo": "Película", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Año": anio, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La película se ha agregado.")

def agregar_serie():
    titulo = input("Ingrese el título de la serie: ")
    actor_principal = input("Ingrese el actor principal de la serie: ")
    director = input("Ingrese el director de la serie: ")
    temporadas = input("Ingrese el número de temporadas de la serie: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    catalogo_productos.append({"Tipo": "Serie", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Temporadas": temporadas, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La serie se ha agregado.")

def agregar_documental():
    titulo = input("Ingrese el título del documental: ")
    director = input("Ingrese el director del documental: ")
    tema = input("Ingrese el tema del documental: ")
    anio = input("Ingrese el año del documental: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    catalogo_productos.append({"Tipo": "Documental", "Título": titulo, "Director": director, "Tema": tema, "Año": anio, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("El documental se ha agregado.")

def agregar_evento_deportivo():
    titulo = input("Ingrese el título del evento deportivo en vivo: ")
    deporte = input("Ingrese el deporte del evento: ")
    fecha = input("Ingrese la fecha del evento: ")
    hora = input("Ingrese la hora del evento: ")
    lugar = input("Ingrese el lugar del evento: ")
    costo_venta = float(input("Ingrese el costo de venta: "))
    catalogo_productos.append({"Tipo": "Evento deportivo en vivo", "Título": titulo, "Deporte": deporte, "Fecha": fecha, "Hora": hora, "Lugar": lugar, "Costo de venta": costo_venta})
    print("El evento deportivo en vivo se ha agregado al catálogo.")
def mostrar_peliculas():
    peliculas = []
    for producto in catalogo_productos:
        if producto["Tipo"] == "Película":
            peliculas.append(producto)

    if peliculas:
        print("Películas:")
        for pelicula in peliculas:
            print_producto(pelicula)
    else:
        print("No hay películas en el catálogo.")


def mostrar_series():
    series = []
    for producto in catalogo_productos:
        if producto["Tipo"] == "Serie":
            series.append(producto)

    if series:
        print("Series:")
        for serie in series:
            print_producto(serie)
    else:
        print("No hay series en el catálogo.")


def mostrar_documentales():
    documentales = []
    for producto in catalogo_productos:
        if producto["Tipo"] == "Documental":
            documentales.append(producto)

    if documentales:
        print("Documentales:")
        for documental in documentales:
            print_producto(documental)
    else:
        print("No hay documentales en el catálogo.")
def mostrar_eventos_deportivos():
    eventos = []
    for producto in catalogo_productos:
        if producto["Tipo"] == "Evento deportivo en vivo":
            eventos.append(producto)

    if eventos:
        print("Eventos deportivos en vivo:")
        for evento in eventos:
            print_producto(evento)
    else:
        print("No hay eventos deportivos en vivo en el catálogo.")


def mostrar_todo():
    if catalogo_productos:
        print("Catálogo completo:")
        for producto in catalogo_productos:
            print_producto(producto)
    else:
        print("El catálogo está vacío.")


def print_producto(producto):
    print(f"Tipo: {producto['Tipo']}")
    print(f"Título: {producto['Título']}")

    if producto['Tipo'] == 'Película' or producto['Tipo'] == 'Serie':
        print(f"Actor principal: {producto.get('Actor principal', 'No hay actor principal')}")

    if producto['Tipo'] == 'Película' or producto['Tipo'] == 'Serie' or producto['Tipo'] == 'Documental':
        print(f"Director: {producto.get('Director', 'No hay director')}")

    if producto['Tipo'] == 'Serie':
        print(f"Temporadas: {producto.get('Temporadas', 'No hay temporadas disponibles')}")

    if producto['Tipo'] == 'Documental':
        print(f"Tema: {producto.get('Tema', 'No hay tema disponible')}")

    if producto['Tipo'] == 'Película' or producto['Tipo'] == 'Documental':
        print(f"Año: {producto.get('Año', 'No hay año disponible')}")

    if producto['Tipo'] == 'Evento deportivo en vivo':
        print(f"Deporte: {producto.get('Deporte', 'No existe deporte o no se puso el deporte')}")
        print(f"Fecha: {producto.get('Fecha', 'No hay fecha')}")
        print(f"Hora: {producto.get('Hora', 'No hay hora')}")
        print(f"Lugar: {producto.get('Lugar', 'No hay lugar')}")

    print(f"Costo de renta: {producto.get('Costo de renta', 'No esta en renta')}")
    print(f"Costo de venta: {producto.get('Costo de venta', 'No esta en venta')}")
#Se hace la funcion para buscar producto
def buscar_producto():
    clave = input("Ingrese palabra clave: ")
    resultados = []

    for producto in catalogo_productos:
        if clave.lower() in producto["Título"].lower():
            resultados.append(producto)

    if len(resultados) > 0:
        print(f"Se encontraron {len(resultados)} resultado(s) que coinciden con la búsqueda:")
        for producto in resultados:
            print(f"Tipo: {producto['Tipo']}")
            print(f"Título: {producto['Título']}")
    else:
        print("No se encontraron productos con la búsqueda.")