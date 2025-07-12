"""
Tienes un fichero ventas.csv que contiene datos de ventas en formato CSV.

Cada línea del fichero tiene la siguiente estructura: 
    fecha,producto,cantidad,precio_unitario 
    
Debes leer el fichero, procesar los datos y calcular el total de ventas por producto. 

Finalmente, debes escribir los resultados en un nuevo fichero total_ventas.txt
"""


RUTA_ARCHIVO = '/workspaces/ProgramacionPython202506/Modulo4/src/ventas.csv'

def obtener_productos(ventas:list)->list:

    lista = list()
    for venta in ventas:
        dicx_venta = dict()

        datos_venta = venta.strip().split(',')

        dicx_venta['fecha'] = datos_venta[0]
        dicx_venta['producto'] = datos_venta[1]
        dicx_venta['cantidad'] = int(datos_venta[2])
        dicx_venta['precio_unitario'] = float(datos_venta[3])

        # subtotal
        dicx_venta['sub_total'] = int(datos_venta[2]) * float(datos_venta[3])

        lista.append(dicx_venta)
    return lista

# 1. Leer archivo
# '2024-07-01,producto1,2,10.50\n'
ventas_txt = open(RUTA_ARCHIVO).readlines()

# obtenemos un listado de diccionario por campo a emplear
ventas = obtener_productos(ventas_txt)

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
    escribir.append('{producto},{total}\n'.format(producto=producto, total=total))


# escribiendo total_ventas -> producto,total
ruta_escritura = '/workspaces/ProgramacionPython202506/Modulo4/src/total_ventas.txt'
with open(ruta_escritura, mode='w') as f:
    f.writelines(escribir)






