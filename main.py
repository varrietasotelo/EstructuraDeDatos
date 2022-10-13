""""

PROGRAMACION DE SOFTWARE
APRENDIZ: VALENTINA ARRIETA SOTELO 
ESTRUCTURAS DE DATOS 

1. LISTAS
Cuentan con varios metodos, entre ellos: 

1.1 append: permite agregar un item al final de la lista.

"""

listVal = ['orange', 'apple', 'kiwi', 'banana']

listVal.append('orange')

print(listVal)
"""
1.2 insert: inserta un item en una posicion determinada. 
"""
listVal.insert(1, 'valen')

print(listVal)
"""
1.3 extend: permite agregar varios elementos a una lista. 
"""
List2 = ['dia', 'noche']

listVal.extend(List2)

print(listVal)
"""
1.4 remove: elimina el elemento de la lista que le indiquemos. 

"""
listVal.remove('dia')

print(listVal)
"""
1.5 pop: elimina de la lista el elemento que se encuentre en la posicion que le indiquemos, y regresa este elemento en la consola. 
"""
listVal.pop(2)

print(listVal)
"""
1.6 clear: elimina todos los elementos de la lista. 
"""
List2.clear()

print(List2)
"""
1.7 index: 

retorna la posicion del primer elemento que sea igual al solicitado. 

si se le indica una posicion retorna la posicion del primer elemento igual al solicitado despues de una posicion dada. 
"""
print(listVal.index('orange'))

print(listVal.index('orange', 2))
"""
1.8 count: retorna el numero de veces que un item se encuentra en la lista 
"""
print(listVal.count('orange'))
"""
1.9 sort: ordena los elementos de la lista. 
"""
ListOrdenada = sorted(listVal)

print(ListOrdenada)
"""
1.10 reverse: invierte los elementos de la lista. 
"""
listVal.reverse()
print(listVal)
"""
1.11 copy: retorna una copia de la lista. 
"""
newListVal = listVal.copy()
print(newListVal)
"""
1.12. utilizar una lista como pila

es muy facil utilizar la lista como una pila, el ultimo elemento agregado sera el primero en ser eliminado.

"""
newListVal.pop()

print(newListVal)

newListVal.pop()

print(newListVal)
"""
1.13. Utilizar una lista como cola

es posible utilizar la lista como cola, de esta forma el primer elemento en la lista sera el primero en ser eliminado. 
"""
from collections import deque

ListCola = deque(["valentina", "josefina", "valeria", "marcos"])

ListCola.popleft()

print(ListCola)
"""
1.14. comprension de las listas 

permite crear nuevas listas donde cada elemento es el resultado de operaciones aplicadas a items de una primera lista, igualmente permiten crear un segmento de la secuencia de esos elementos para cumplir determinada condicion. 
"""

cuadrado = []
for x in range(5):
  cuadrado.append(x**2)

print(cuadrado)
"""
esto tambien se puede lograr mediante la siguiente sintaxis
"""

cuadrado1 = [x**2 for x in range(5)]
print(cuadrado1)
"""
las listas de comprension se encunetran conformadas por una expresion junto a una expresion for y luego 0 o mas declaraciones for o if.

en la siguiente expresion se combinaran los dos grupos (x, y)
"""

comprension = [(x, y) for x in [1, 2, 3] for y in [5, 1, 2]]

print(comprension)
"""
las comprensiones de las listas pueden estar conformadas por expresiones complejas y funciones anidadas
"""

num = [-5, -3, -1, 0, 2, 3, 5]
num2 = [x * 3 for x in num]
print(num2)

#crear un filtro en una lista que no incluya numeros negativos

numPositivos = [x for x in num2 if x >= 0]

print(numPositivos)
"""
1.5 Listas por comprension anidadas 

primero se implementa una max de 3x4, y seguidamente se crearan nuevos grupos segun las filas de la matriz. 
"""

matriz = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]

matrizRow = [[row[i] for row in matriz] for i in range(4)]
print(matrizRow)

#otra forma de realizarlo es a traves de la funcion zip()

matrizRow1 = list(zip(*matriz))

print(matrizRow1)
"""
2. La instruccion DEL 

Esta instruccion permite retirar un item de una lista indicando su indice-posicion, tambien permite retirar secciones de la lista o vaciarla. 
"""

list = [-2, 5, 2, 10, 53, 5]
del list[0]
print(list)

#cuando se elimina una seccion incluira el valor determinado al final de la seccion
del list[1:3]
print(list)

#de esta forma se elimina todo lo que se encuentra en la lista
del list[:]
print(list)

#igualmente puede utilizarse para eliminar variables

del list
"""
3. Tuplas o secuencias

las listas, tuplas y cadenas son datos de tipo secuencia.

la tupla es un numero de valores separados por comas. 
"""

T = 2, 3, 4, 'valentina'
print(T)

#las tuplas pueden ser anidadas

T1 = T, (4, 8, 6, 78)
print(T1)

#las tuplas son inmutables

#las tuplas se pueden crear vacias al representarlas con un parentesis

vacio = ()
print(len(vacio))

#para crear una tupla de un solo elemento se debera colocar una coma despues del elemento

uno = 1,
print(uno)

#los elementos de una tupla son heterogeneos, generalmente son accedidos para "desempacar" o indexar

#desempacar una tupla implica acceder a deteminados elementos de la misma, esto se puede lograr mediante un indice.

tupla = (10, 20, 30, 40, 50)
primero, segundo, ultimo = tupla[0], tupla[1], tupla[-1]

print(primero, segundo, ultimo)
"""
4. Conjuntos 

son colecciones no ordenadas y sin elementos repetidos, permiten la verificacion de pertenencia y eliminacion de duplicados. 

tambien permite la union, interseccion, diferencia y diferencia simetrica. 

se pueden crear a traves de la funcion set() para crear un conjunto vacio. 

para crear un conjunto utilizamos las llaves {}
"""

conjunto = {1, 5, 2, 5, 8, 'valen'}
print(conjunto)

#crear conjuntos de un solo elemento

a = set('uno')
b = set('unanime')

#para revisar los elementos unicos en un conjunto
print(a)

#para encontrar las letras que se encuentran en a pero no en b
print(a - b)

#para encontrar las letras que se encuentran en a, b o los dos
print(a | b)

#para encontrar las letras presentes en a y b
print(a & b)

#para encontrar las letras en a o b, pero no en las dos
print(a ^ b)

#los conjuntos tambien permiten su comprension
#el siguiente codigo nos muestra las letras presentes en c que no son abc
c = {x for x in 'abracadabra' if x not in 'abc'}
"""
5. Diccionarios

son memorias asociativas o arreglos asociativos, son indexados con claves que pueden ser de cualquier tipo inmutable. 

las claves pueden ser: cadenas, numeros, tuplas (siempre que contengan cadenas, numeros o tuplas. si contiene un elemento mutable no puede usarse como clave).

las listas no pueden ser usadas como claves, ya que estas pueden modificarse. 

para crear un diccionario vacio se utilizan {} vacias
"""
personas = {'valentina': 1, 'valeria': 2}

personas['juan'] = 3

print(personas)

#los diccionarios tambien permiten la instruccion del
del personas['juan']
print(personas)

#el constructor dict() crea secuencias de pares en un diccionario
d = dict([('valen', 1), ('valeria', 2), ('juan', 3)])
print(d)

#la comprension en diccionarios permite crear diccionarios con expresiones arbitrarias

#la siguiente expresion crea un diccionario con los valores al cuadrado de los numeros indicados junto a su respectivo valor inicial
e = {x: x**2 for x in (4, 6, 10)}
print(e)

#cuando se trata de cadenas simples se pueden especificar los pare utilizando =
f = dict(valentina=1, juan=2, jorge=3)
print(f)
"""
6. Iteracion 
"""

#los diccionarios se puede iterar mediante el metodo items(), este permite observar la clave y su valor.

g = {'valentina': 1, 'valeria': 2}
for a1, a2 in g.items():
  print(a1, a2)

#al iterar una secuencia se puede objeter su posicion-indice junto al valor usando la funcion enumerate()

for a2, b2 in enumerate(['val', 'ux', 'dye']):
  print(a2, b2)

#para iterar dos secuencias al tiempo se utiliza la funcion zip()

estudiantes = ['nombre', 'edad', 'color favorito']
respuestas = ['marcos', 22, 'verde']
for a3, a4 in zip(estudiantes, respuestas):
  print('cual es tu {0}? es {1}'.format(a3, a4))

#para iterar una secuencia de forma inversa , se especifica la secuencia y luego se llama la funcion reversed()

for a4 in reversed(range(4, 5, 8)):
  print(a4)

"""
7. Condiciones 
las condiciones mas usadas son if y while. 

los operadores de comparacion in y not determinan que valores se encuentran o no. 

las comparaciones pueden concatenarse y combinarse mediante los operadores booleanos and y or. 
"""
a11, a12, a13 = '', 'valentina', 'sotelo'
non_null = a11 or a12 or a13
print(non_null)
