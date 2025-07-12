"""
Emplear mongo db para insertar varios valores en una colección "ventas"

"""

from pymongo import MongoClient
from pprint import pprint


def conexion_mongo_db(cadena_conexion, db_name):    
    """
    Establece una conexión a la base de datos MongoDB y devuelve el objeto de la base de datos.
    
    :param cadena_conexion: Cadena de conexión a MongoDB.
    :param db_name: Nombre de la base de datos a la que se desea conectar.
    :return: Objeto de la base de datos MongoDB.
    """
    try:
        cliente = MongoClient(cadena_conexion)
        db = cliente[db_name]
        print(f"Conexión exitosa a la base de datos '{db_name}'")
        return db
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


# Cadena de conexión a MongoDB
cadena_conexion_mongo = "mongodb+srv://gon2794:62K1cb1yRQ2CL1Gd@cluster0.fu6aoxm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Conectar a la base de datos 'ventas'
db_ventas = conexion_mongo_db(cadena_conexion=cadena_conexion_mongo, db_name='curso_db')


cantidad_insertar = int(input("¿Cuántas ventas desea insertar? "))


for i in range(cantidad_insertar):

    print('='*30+f'Inserción de venta número: {i+1}' +'='*30)

    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    precio = float(input("Ingrese el precio del producto: "))

    # Crear un diccionario con los datos de la venta
    venta = {
        'fecha': fecha,
        'producto': producto,
        'cantidad': cantidad,
        'precio': precio
    }

    # Insertar la venta en la colección 'ventas'
    db_ventas.ventas.insert_one(venta)



# Verificar las ventas insertadas
ventas = list(db_ventas.ventas.find())
print("\nVentas insertadas:")

pprint(ventas)

