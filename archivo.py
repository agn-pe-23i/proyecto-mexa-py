#Importamos  el catalogo
import catalogo
#Hacemos una funcion para cargar catalago donde va a leer el archivo.txt
def cargar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            catalogo.catalogo_productos = eval(archivo.read())
        print("El catálogo se ha cargado.")
    except FileNotFoundError:
        print("catalogo no existe.")
    except:
        print("Ocurrió un error.")
#Hacemos una funcion para que guarde el catalogo y lo ponga en un archivo .txt
def guardar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(str(catalogo.catalogo_productos))
        print("Se ha guardado correctamente.")
    except:
        print("Ocurrió un error.")