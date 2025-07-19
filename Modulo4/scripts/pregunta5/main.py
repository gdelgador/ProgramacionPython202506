"""
Empleando el ejercicio visto en clase de Procesamiento con Ficheros. 
Supongamos que el precio brindado en el archivo “ventas.csv”  ha sido dato en dolares. 

Deberá solarizar el precio según la fecha de compra, para esto deberá leer la información 
almacenada de tipo de cambio de la base mongodb o sqlite (elegir una). 

Posteriormente debera obtener el precio total vendido (solarizado) por producto. 
Finalmente almacene dicha información en una colección de mongo db.
"""
from pymongo import MongoClient
from typing import List, Dict


# Conexion MONGO DB, contraseñas no deben ir en el código
RUTA_CADENA_CONEXION = "/workspaces/ProgramacionPython202506/Modulo4/scripts/problema4/cadena.txt"
RUTA_ARCHIVO = '/workspaces/ProgramacionPython202506/Modulo4/src/ventas.csv'
CADENA_CONEXION_MONGO_DB = open(RUTA_CADENA_CONEXION).read().strip()

class SUNAT:
    """
    Clase para obtener valos de la coleccion sunat
    """
    def __init__(self, cadena_conexion, db_consulta):
        self.db = self.conexion_mongo_db(cadena_conexion=cadena_conexion, db_name=db_consulta)    
        pass

    def conexion_mongo_db(self, cadena_conexion:str, db_name:str):
        client = MongoClient(cadena_conexion)
        db = client[db_name]
        return db
    
    def get_data_by_date(self, fecha:str):
        return list(self.db.sunat.find({"fecha": fecha}))

    def insert_into_collection(self, collection_name:str, listado_insertar:List[Dict]):
        """Inserta Registro dentro de una coleccion"""

        print('Insertando {cantidad} registros'.format(cantidad=len(listado_insertar)))
        self.db[collection_name].insert_many(listado_insertar)
    pass



def obtener_productos(ventas:list, sunat:SUNAT)->list:
    lista = list()
    for venta in ventas:
        dicx_venta = dict()

        datos_venta = venta.strip().split(',')

        dicx_venta['fecha'] = datos_venta[0]
        dicx_venta['producto'] = datos_venta[1]
        dicx_venta['cantidad'] = int(datos_venta[2])

        # precio unitario dolares
        dicx_venta['precio_unitario_dolares'] = float(datos_venta[3])
        
        tc_data = sunat.get_data_by_date(dicx_venta['fecha'])

        # agregamos datos del tipo cambio venta
        dicx_venta['tc'] = tc_data[0]['venta']

        # solarizando precio unitario
        dicx_venta['precio_unitario_soles'] = dicx_venta['precio_unitario_dolares'] * dicx_venta['tc']

        # subtotal solarizado
        dicx_venta['sub_total'] = dicx_venta['cantidad'] * dicx_venta['precio_unitario_soles']

        lista.append(dicx_venta)
    return lista

def main():

    # Genero una clase y obtengo datos de la base de datos x fecha
    sunat = SUNAT(CADENA_CONEXION_MONGO_DB, 'curso_db')

    # lectura archivo ventas
    ventas_txt = open(RUTA_ARCHIVO).readlines()
    ventas = obtener_productos(ventas_txt, sunat)


    # diccionario para obtener productos
    productos = dict()
    for venta in ventas: 
        producto = venta['producto']
        sub_total = venta['sub_total']
        
        # agrego llave a diccionario
        if not producto in productos.keys():
            productos[producto] = sub_total
            continue

        # si llave existe, se realiza una suma del sub_total
        productos[producto] += sub_total
        pass

    # formato para escribir
    escribir = []
    for producto, total in productos.items():
        escribir.append('{producto},{total:.2f}\n'.format(producto=producto, total=total))

    # escribiendo total_ventas -> producto,total
    ruta_escritura = '/workspaces/ProgramacionPython202506/Modulo4/scripts/pregunta5/total_ventas.txt'
    with open(ruta_escritura, mode='w') as f:
        f.writelines(escribir)
    pass



if __name__ == '__main__':
    main()
