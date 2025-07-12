"""
1. En este ejercicio deberás crear un script llamado <code>personas.py</code> 
que lea los datos de un fichero de texto <code>personas.txt</code>, 
que transforme cada fila en un diccionario y lo añada a una lista llamada personas.


Luego rocorre las personas de la lista y para cada una muestra de forma 
amigable todos sus campos.
"""



RUTA_ARCHIVO = '/workspaces/ProgramacionPython202506/Modulo4/src/personas.txt'


# 1. lectura
with open(RUTA_ARCHIVO) as f:
    lineas_archivo = f.readlines()

# 2. procesamiento
lista_personas = list()
for linea in lineas_archivo:
    dicx_persona = dict()

    # aplico metodos de cadena para limpieza de data
    linea = linea.strip()
    contenido = linea.split(';')

    # agregar al diccionario
    dicx_persona['indice'] = contenido[0]
    dicx_persona['nombre'] = contenido[1]
    dicx_persona['apellido'] = contenido[2]
    dicx_persona['fecha_nacimiento'] = contenido[3]

    # agrego data a lista
    lista_personas.append(dicx_persona)
    pass

# Imprimiendo de forma adecuada
for persona in lista_personas:
    print('--------------------------')
    print('Indice: {indice}\nNombre: {nombre}\nApellido: {apellido}\nFechaNacimiento: {fecha_nacimiento}'.format(**persona) )

