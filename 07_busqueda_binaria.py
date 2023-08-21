import random

def busqueda_binaria(lista, comienzo, final, objetivo):
  # esto es un print statement: y pensar de manera iterativa es esntender muy bien los stack frames, esto es leer recursividad, una vez que lo entiendes es de las cosas mas sencillas, 
  print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')  # si no le pongo el -1 me da IndexError: list index out of range (este es el famoso error de "of by one")
  if comienzo > final: # significa que no esta en la lista porque lo hicimos mas chico, mas chico y no se encontró
    return False

  medio = (comienzo + final) // 2

  if lista[medio] == objetivo:
    return True

  elif lista[medio] < objetivo:
    return busqueda_binaria(lista, medio + 1, final, objetivo)

  else:
    return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

# el profe dice que primero el escribe el siganture osea lo que debe de tener la función y después escribe la fución
if __name__ == '__main__':
  tamano_de_la_lista = int(input('De que tamaño será la lista?: '))
  objetivo = int(input('Que número quieres encontrar? '))

  lista = sorted([random.randint(0,100) for i in range(tamano_de_la_lista)])

  encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

  print(lista)
  print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') # aqui generamos operadores ternarios   al generar un if y else en una misma linea de codigo

# par poder usar comillas dobles o simples en un mismo format debemos escapar usando \