"""
Ingrese la base y la altura de un triangulo, luego realice el calculo del área. Por ultimo muestre el resultado en pantalla
"""

# 1.Ingreso de datos
# funcion "input" -> retorna un "str", si deseo un número debo convertirlo. Por ejemplo a un entero con "int"
base_tringualo = int(input('Ingrese la base del triangulo: '))
altura_triangulo = int(input('Ingrese la altura del triangulo: '))

# 2. Calcular el area del triangulo

area_triangulo = base_tringualo * altura_triangulo /2

# 3. Imprimir Resultado

print(area_triangulo)
# Imprimiendo con "f" format string delante del texto
print(f'El area del triguanlo con base {base_tringualo} y altura {altura_triangulo} es : {area_triangulo}')

print('El area del triguanlo con base {} y altura {} es : {}'.format(base_tringualo, altura_triangulo, area_triangulo))

print('Base {base}\nAltura {altura}\nArea {area}'.format(base=base_tringualo, altura=altura_triangulo, area=area_triangulo))



