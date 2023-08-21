"""
Les dejo un link con mis apuntes https://github.com/karlbehrensg/poo-y-algoritmos-python

Clases de complejidad algorítmica
Existen distintos tipos de complejidad algorítmica:

O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
O(n!) Factorial: crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.
"""

"""
Created on Sun May 10 19:49:22 2020

@author: xavik
"""

# -*- coding: utf-8 -*-

import math
import time 

class Complejidad_algoritmica:
	def __init__(self, n):
		self.n = n

	def constante(self):
		return 1

	def logaritmica(self):
		return math.log10(self.n)

	def lineal(self):
		return self.n

	def log_lineal(self):	
		return self.n * math.log10(self.n)

	def	polinomial(self):
		return self.n**2

	def	exponencial(self):
		return 2**self.n


def main():
	
    nums = [1, 10, 100, 1000, 10000]
    
    for n in nums:
        
        complejidad = Complejidad_algoritmica(n)
        
        print('n es igual a: {}'.format(n))
        
        principio = time.time()
        print(f'El resultado de complejidad constante para n igual a {n} es: ', complejidad.constante())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica para n igual a {n} es: ', complejidad.logaritmica())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad lineal para n igual a {n} es: ', complejidad.lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica lineal para n igual a {n} es: ', complejidad.log_lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad polinomial para n igual a {n} es: ', complejidad.polinomial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
       
        principio = time.time()
        print(f'El resultado de complejidad exponencial para n igual a {n} es: ', complejidad.exponencial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        print('\n\n')
        
	    

if __name__ == '__main__':
    
    main()