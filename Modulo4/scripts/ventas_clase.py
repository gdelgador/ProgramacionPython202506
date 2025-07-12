RUTA_ARCHIVO = '/workspaces/ProgramacionPython202506/Modulo4/src/ventas.csv'


class Producto:
    def __init__(self, nombre:str, precio:float):
        self.producto = nombre
        self.precio = precio

        self.total_venta = 0

    def total_venta_producto(self, monto):
        return self.total_venta + monto

class Venta(Producto):
    def __init__(self,fecha,nombre,precio,cantidad):
        # producto
        super().__init__(nombre, precio)

        self.fecha = fecha
        self.cantidad = cantidad
        self.sub_total = self.obtener_subtotal()

    def obtener_subtotal(self):
        return self.cantidad * self.precio
    



def obtener_productos(ventas:list)->list:
    lista = list()
    for venta in ventas:
        datos_venta = venta.strip().split(',')

        fecha = datos_venta[0]
        producto = datos_venta[1]
        cantidad = int(datos_venta[2])
        precio_unitario = float(datos_venta[3])

        lista.append(Venta(fecha, producto, precio_unitario, cantidad))
    return lista


# 1. Lectura archivo
ventas_txt = open(RUTA_ARCHIVO).readlines()

# Obtendria una lista de Ventas
ventas = obtener_productos(ventas_txt)


productos = dict()

for venta in ventas:

    producto = venta.producto
    sub_total = venta.sub_total

    if not producto in productos.keys():
        productos[producto] =  venta.total_venta_producto(sub_total)
        continue
    productos[producto] +=venta.total_venta_producto(sub_total)
    

print(productos)
