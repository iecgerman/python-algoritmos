"""
El ordenamiento por inserción es uno de los algoritmos más comunes que estudian
los Científicos del Cómputo. Es intuitivo y fácil de implementar, pero es muy
ineficiente para listas de gran tamaño.

Una de las características del ordenamiento por inserción es que ordena en “su
lugar.” Es decir, no requiere memoria adicional para realizar el ordenamiento
ya que simplemente modifican los valores en memoria.

La definición es simple:

Una lista es dividida entre una sublista ordenada y otra sublista desordenada.
Al principio, la sublista ordenada contiene un solo elemento, por lo que por
definición se encuentra ordenada.

A continuación se evalua el primer elemento dentro la sublista desordenada para
que podamos insertarlo en el lugar correcto dentro de la lista ordenada.

La inserción se realiza al mover todos los elementos mayores al elemento que
se está evaluando un lugar a la derecha.

Continua el proceso hasta que la sublista desordenada quede vacia y, por lo
tanto, la lista se encontrará ordenada.

Veamos un ejemplo:

Imagina que tienes la siguiente lista de números:

7, 3, 2, 9, 8

Primero añadimos 7 a la sublista ordenada:

7, 3, 2, 9, 8

Ahora vemos el primer elemento de la sublista desordenada y lo guardamos en
una variable para mantener el valor. A esa variable la llamaremos valor_actual.
Verificamos que 3 es menor que 7, por lo que movemos 7 un lugar a la derecha.

7, 7, 2, 9, 8 (valor_actual=3)

3 es menor que 7, por lo que insertamos el valor en la primera posición.

3, 7, 2, 9, 8

Ahora vemos el número 2. 2 es menor que 7 por lo que lo movemos un espacio a la
derecha y hacemos lo mismo con 3.

3, 3, 7, 9, 8 (valor_actual=2)

Ahora insertamos 2 en la primera posición.

2, 3, 7, 9, 8

9 es más grande que el valor más grande de nuestra sublista ordenada por lo que
lo insertamos directamente en su posición.

2, 3, 7, 9, 8

El último valor es 8. 9 es más grande que 8 por lo que lo movemos a la derecha:

2, 3, 7, 9, 9 (valor_actual=8)

8 es más grande que 7, por lo que procedemos a insertar nuestro valor_actual.

2, 3, 7, 8, 9

Ahora la lista se encuentra ordenada y no quedan más elementos en la sublista
desordenada.

Antes de ver la implementación en Python, trata de implementarlo por ti mismo
y compártenos tu algoritmo en la sección de comentarios.

Esta es una forma de implementar el algoritmo anterior:
"""

import random

def ordenamiento_insercion(lista):
    # crea un contador segun el largo de la lista para usar el indice como cursor
    for indice in range(1, len(lista)):
        # guarda el valor actual del cursor en una variable
        valor_actual = lista[indice] # ej: (5)
        # si el cursor es mayor que cero
        # y el numero anterior al cursor es mayor que el valor actual
        while indice > 0 and lista[indice - 1] > valor_actual: # ej: 7 > (5)?
            # el valor actual pasa a ser igual al numero anterior al cursor
            lista[indice] = lista[indice -1] # ej: [...7,(5)...] => [...7,(7)...]
            # se resta 1 al indice para posarnos en el numero anterior al cursor
            indice -= 1 # ej: [...(7),7...]
        # como insertamos el valor del numero anterior al cursor en la posicion actual,
        # ahora insertamos en la posicion del numero anterior, el valor que teniamos guardado
        lista[indice] = valor_actual # ej: [...(7),7...] => [...(5),7...]
        # y seguimos con el siguiente indice.
    return lista

if __name__=='__main__':
  tamano_de_la_lista = int(input('De que tamaño será la lista?: '))
  lista = [random.randint(0,100) for indice in range(tamano_de_la_lista)]
  print("Lista Desordenada: ")
  print(lista)
  print("empezemos a ordenar: ")
  
  lista_ordenada = ordenamiento_insercion(lista)
  print(lista_ordenada)