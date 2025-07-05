"""
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.
"""

# Inicializamos la serie de fibonacci con los 2 primeros valores de esta

def mostrar_serie_fibonacci():
    """Imprime la serie de fibonacci en el rango [0-50]"""

    numeros_fibonacci = [0,1]

    c = 0
    while c<=50:
        # "c" <- suma de 2 ultimos valores de nuestra serie
        c = numeros_fibonacci[-1] + numeros_fibonacci[-2]

        # break -> comando de salida del bucle
        if c>50:
            break
        numeros_fibonacci.append(c)

    # Mostramos la serie de Fibonacci
    print('Mostrando la serie de Fibonacci entre 0 y 50')
    print(numeros_fibonacci)
    pass

mostrar_serie_fibonacci()
























