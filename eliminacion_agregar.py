import catalogo
#Hacemos la funcion para eliminar producto
def eliminar_producto():
    titulo = input("Ingrese el título del producto que desea eliminar: ")

    for producto in catalogo.catalogo_productos:
        if producto["Título"] == titulo:
            catalogo.catalogo_productos.remove(producto)
            print("El producto fue eliminado.")
            return

    print("No se encontró producto.")
#Hacemos la funcion para el menu agregar
def menu_agregar():
    print("Menú agregar producto")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Evento deportivo en vivo")
    print("5. Regresar")

    opcion = input("Seleccione una opción: ")

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
#Hacemos varias funciones ya sea para agregar peliculas, series etc
def agregar_pelicula():
    titulo = input("Ingrese el título de la película: ")
    actor_principal = input("Ingrese el actor principal de la película: ")
    director = input("Ingrese el director de la película: ")
    anio = input("Ingrese el año de la película: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    catalogo.catalogo_productos.append({"Tipo": "Película", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Año": anio, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La película se ha agregado.")

def agregar_serie():
    titulo = input("Ingrese el título de la serie: ")
    actor_principal = input("Ingrese el actor principal de la serie: ")
    director = input("Ingrese el director de la serie: ")
    temporadas = input("Ingrese el número de temporadas de la serie: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    catalogo.catalogo_productos.append({"Tipo": "Serie", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Temporadas": temporadas, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La serie se ha agregado.")

def agregar_documental():
    titulo = input("Ingrese el título del documental: ")
    director = input("Ingrese el director del documental: ")
    tema = input("Ingrese el tema del documental: ")
    anio = input("Ingrese el año del documental: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    catalogo.catalogo_productos.append({"Tipo": "Documental", "Título": titulo, "Director": director, "Tema": tema, "Año": anio, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("El documental se ha agregado.")

def agregar_evento_deportivo():
    titulo = input("Ingrese el título del evento deportivo en vivo: ")
    deporte = input("Ingrese el deporte del evento: ")
    fecha = input("Ingrese la fecha del evento: ")
    hora = input("Ingrese la hora del evento: ")
    lugar = input("Ingrese el lugar del evento: ")
    costo_venta = float(input("Ingrese el costo de venta: "))
    catalogo.catalogo_productos.append({"Tipo": "Evento deportivo en vivo", "Título": titulo, "Deporte": deporte, "Fecha": fecha, "Hora": hora, "Lugar": lugar, "Costo de venta": costo_venta})
    print("El evento deportivo en vivo se ha agregado al catálogo.")