import random

def busqueda_lineal(lista, objetivo):
  match = False

  for elemento in lista: # <- la complejidad algorítmica que aquí tenemos es un O(n)
    if elemento == objetivo:
      match = True
      break

  return match

if __name__ == '__main__':
  tamano_de_la_lista = int(input('De que tamaño será la lista?: '))
  objetivo = int(input('Que número quieres encontrar? '))

  lista = [random.randint(0,100) for i in range(tamano_de_la_lista)]

  encontrado = busqueda_lineal(lista, objetivo)

  print(lista)
  print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') # aqui generamos operadores ternarios   al generar un if y else en una misma linea de codigo

# par poder usar comillas dobles o simples en un mismo format debemos escapar usando \