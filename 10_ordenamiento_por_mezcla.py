import random

def ordenamiento_por_mezcla(lista):
  if len(lista) > 1:
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    print(izquierda, "*****", derecha)

    # llamada recursiva en cada mitad
    ordenamiento_por_mezcla(izquierda)
    ordenamiento_por_mezcla(derecha)

    # Iteradores para recorrer las dos sublistas
    i = 0
    j = 0
    # Iterador para la lista principal
    k = 0

    while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:  # ejemplo si 7 < 8 
        lista[k] = izquierda[i]
        i += 1
      else:
        lista[k] = derecha[j]
        j += 1

      k += 1 # esto es para que el while no se vaya al infinito

    while i < len(izquierda):
      lista[k] = izquierda[i]
      i += 1
      k += 1

    while j < len(derecha):
      lista[k] = derecha[j]
      j += 1
      k += 1

    print(f'izquierda {izquierda}, derecha {derecha}')
    print(lista)
    print('-' * 50)

  return lista


if __name__ == '__main__':
  tamano_de_la_lista = int(input('De que tamaño será la lista?: '))

  lista = [random.randint(0,100) for i in range(tamano_de_la_lista)]
  print("Lista Desordenada: ")
  print(lista)
  print("-" * 20)
  print("empezemos a ordenar: ")
  
  lista_ordenada = ordenamiento_por_mezcla(lista)
  print("lista ordenada: ")
  print(lista_ordenada)

"""
Les comparto la explicación de ChatGPT WOW

¡Por supuesto! El código que has compartido implementa el algoritmo de ordenamiento por mezcla (merge sort) de manera recursiva. Este algoritmo divide la lista en mitades más pequeñas, ordena esas mitades y luego las combina en una lista ordenada. Aquí tienes una explicación paso a paso de cómo funciona el código:

Se importa el módulo random, que se utilizará para generar números aleatorios.
Se define la función ordenamiento_por_mezcla(lista) que implementa el algoritmo de ordenamiento por mezcla. Esta función toma una lista como entrada y la ordena.
La función comienza verificando si la longitud de la lista es mayor que 1. Si la longitud es 1 o menor, la lista se considera ordenada y se retorna tal cual.
Si la longitud es mayor que 1, la función encuentra el punto medio de la lista (medio) y divide la lista en dos partes: izquierda y derecha.
Luego, la función imprime las sublistas izquierda y derecha para mostrar cómo se están dividiendo en cada iteración.
Se realiza una llamada recursiva a ordenamiento_por_mezcla(izquierda) para ordenar la mitad izquierda de la lista, y otra llamada recursiva a ordenamiento_por_mezcla(derecha) para ordenar la mitad derecha de la lista.
Después de que ambas mitades estén ordenadas, se realiza el proceso de fusión (merge) de las dos mitades ordenadas en una lista ordenada completa.
Se utilizan tres iteradores: i para la mitad izquierda, j para la mitad derecha y k para la posición en la lista principal.
Se compara el elemento actual en las sublistas izquierda[i] y derecha[j], y se coloca el elemento más pequeño en la posición k de la lista principal. Luego, se incrementa el iterador correspondiente y el iterador k.
Se repite el paso 9 hasta que se hayan recorrido completamente ambas sublistas.
Si aún quedan elementos en alguna de las sublistas después de salir del bucle anterior, se agregan a la lista principal.
Finalmente, se imprime el estado de las sublistas izquierda y derecha, la lista principal ordenada y una línea de guiones para separar visualmente los resultados.
La función retorna la lista principal ordenada.
En la parte final del código, se verifica si el script se está ejecutando como el programa principal (no importado como módulo). Se solicita al usuario ingresar el tamaño de la lista a ordenar.
Se crea una lista llamada lista que contiene números aleatorios entre 0 y 100. La cantidad de números en la lista es igual al tamaño especificado por el usuario.
Se imprime la lista original.
Se llama a la función ordenamiento_por_mezcla(lista) para ordenar la lista.
Se imprime la lista ordenada resultante.
En resumen, este código implementa el algoritmo de ordenamiento por mezcla utilizando recursión para dividir y combinar sublistas, lo que resulta en una lista principal ordenada al final.
"""