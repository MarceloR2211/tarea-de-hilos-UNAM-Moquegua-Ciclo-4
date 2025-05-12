"""
 4. Ejercicio de Sincronización con Hilos: Cálculo de
 Media
 Enunciado: Crea un programa en Python que divida el cálculo de la media
 de una lista de 1 millón de números en dos hilos. Cada hilo debe calcular la
 suma de la mitad de la lista y luego combinar los resultados. Utiliza Lock
 para sincronizar el acceso a las variables compartidas.
 Pistas:
 • Usa dos hilos para dividir el trabajo.
 • Calcula la suma de cada mitad y divide entre el número total de ele
mentos.
"""
from threading import Thread
import random

total = [0]
lista = [random.randint(1, 1000000) for _ in range(1000000)]

def sumas(inicio, fin):
    partial_sum = 0
    for i in range(inicio, fin):
        partial_sum += lista[i]
    total[0] += partial_sum
h1 = Thread(target=sumas, args=(0, 500000))
h2 = Thread(target=sumas, args=(500000, 1000000))

h1.start()
h2.start()

h1.join()
h2.join()
print("total:", total[0]/1000000)