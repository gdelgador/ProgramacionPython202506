"""
Del ejercicio de Clase. Emplee el API de SUNAT que corresponda para obtener el precio de compra y venta del dólar durante todo el 2023. Almacene dicha información en base de datos sqlite ‘base.db’ con nombre de tabla sunat_info y en mongo db.
Finalmente deberá mostrar el contenido de dicha tabla.
Lee la documentación del API: https://apis.net.pe/api-tipo-cambio.html
"""

import requests
from pymongo import MongoClient
import time 

# Conexion MONGO DB, contraseñas no deben ir en el código
RUTA_ARCHIVO = "/workspaces/ProgramacionPython202506/Modulo4/scripts/problema4/cadena.txt"

CADENA_CONEXION_MONGO_DB = open(RUTA_ARCHIVO).read().strip()
URL = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month={month}&year={year}"


# Genero mis funciones
def obtener_tipo_cambio(month:int, year:int)->list:
    """
    Obtener tipo de cambio SUNAT
    """
    try:
        response = requests.get(URL.format(month=month, year=year))

        if response.status_code!=200:
            print('Error al obtener solicitud ...')
            return []
        return response.json()
    except requests.RequestException:
        return []
    pass

def conexion_mongo_db(cadena_conexion:str, db_name:str):
    client = MongoClient(cadena_conexion)
    db = client[db_name]
    return db

def main():

    # conexion a base de datos de mongo db
    db_curso = conexion_mongo_db(cadena_conexion=CADENA_CONEXION_MONGO_DB, db_name='curso_db')

    for codmes in range(1, 13):
        print(f'Obteniendo tipo cambio mes {codmes} ...')
        listado_sunat = obtener_tipo_cambio(month=codmes, year=2024)

        # almacenar en bd Mongo DB
        print('Insertando {cantidad} registros'.format(cantidad=len(listado_sunat)))
        db_curso.sunat.insert_many(listado_sunat)

        # tiempo de espera
        time.sleep(2)

    print('Proceso Finalizado!!')
    pass


# Llamo a funcion main
if __name__ == "__main__":
    main()
    pass 