"""
7. Ejercicio de Programación en Memoria Compartida:
 Cálculo de Productos
 Enunciado: Escribe un programa en Python que use dos hilos para calcular
 el producto de los elementos de dos listas de números. Cada hilo debe calcular
 el producto de la mitad de los elementos y luego combinar los resultados.
 Pistas:
 • Utiliza dos listas de números.
 • Usa Thread y Lock para manejar el acceso concurrente a las variables
"""
from threading import Thread, Lock
import random
lock=Lock()

tamano = int(input("ingrese el tamano de la lista: "))
total = [0]
lista1 = [random.randint(1, tamano) for _ in range(tamano)]
lista2 = [random.randint(1, tamano) for _ in range(tamano)]

def sumas( inicio, fin):

    partial_sum = 0
    for i in range(inicio, fin):
        partial_sum += lista1[i]*lista2[i]
    with lock:
        total[0] += partial_sum
    

h1=Thread(target=sumas, args=(0,tamano//2))
h2=Thread(target=sumas, args=(tamano//2,tamano))
h1.start()
h2.start()
h1.join()
h2.join()
print("total:", total[0])