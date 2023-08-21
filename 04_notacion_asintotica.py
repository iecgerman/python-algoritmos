"""
Estoy muy metido en el mundo de programacion competitiva, y en este ambito de la programacion es muy, muy importante entender el Big O notation para poder tener soluciones eficientes a los problemas dados.
"""

Notacion asintótica

Big O notation.

Crecimiento asintótico

No importan las variaciones pequeñas.

El enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito

Mejor de los casos, promedio, peor de los casos.

Nada más importa el término de mayor tamaño.

Ejemplos:

def f(n)
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

O(n) + O(n) = O(n+n) = O(2n) = O(n) //Crecimiento lineal

def f(n)
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

O(n) + O(n*n) = O(n+n) = O(n + n^2) = O(n^2) //Crecimiento exponencial

def f(n) # aquí hay un loop dentro de otro loop o una iteración dentro de otra iteración
    for i in range(n):
        for j in range(n):
            print(i,j)

O(n) O(n) = O(nn) = O(n^2) //Crecimiento exponencial

def fibonacci(n):
    if n == 0 or n ==1:
        return 1

     return fibonacci(n - 1) + fibonacci(n - 2)

O(2**n) //tiene varias llamadas recursivas y eso hace al algoritmo con un crecimiento exponencial