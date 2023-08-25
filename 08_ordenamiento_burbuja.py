import random

def ordenamiento_de_burbuja(lista):
  n = len(lista)

  for i in range(n):
    for j in range(0, n - i - 1): # O(n) = O(n * n) = O(n**2)

      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j] # con esto estamos inter cambiando cada uno de los elementos, se ve complicado pero esta fácil
        print(lista)
        #print("------")

  return lista


if __name__ == '__main__':
  tamano_de_la_lista = int(input('De que tamaño será la lista?: '))

  lista = [random.randint(0,100) for i in range(tamano_de_la_lista)]
  print("Lista Desordenada: ")
  print(lista)
  print("empezemos a ordenar: ")
  
  lista_ordenada = ordenamiento_de_burbuja(lista)
  print("lista ordenada: ")
  print(lista_ordenada)

"""
Ordenamiento de burbuja (BUBBLE SORT)

El primer algoritmo de ordenamiento que veremos es el ordenamiento de burbuja. Es un algoritmo que recorre repetidamente una lista que necesita ordenarse. Compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este procedimiento se repite hasta que no se requiere mas intercambios, lo que indica que la lista se encuentra ordenada.
"""