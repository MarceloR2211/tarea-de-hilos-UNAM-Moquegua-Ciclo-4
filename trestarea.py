"""
 3. Ejercicio de Condiciones de Carrera: Suma en Paralelo
 Enunciado: Escribe un programa en Python que sume los elementos de
 una lista de 10 millones de números usando dos hilos. Inicialmente, cada hilo
 sumará una mitad de la lista, pero sin sincronización. Identifica y explica los
 posibles errores que podrían surgir debido a la falta de sincronización.
 Pistas:
 • Utiliza Thread sin ningún tipo de sincronización (sin Lock).
 • Observa los resultados y discútelos
"""
from threading import Thread
import random

total = [0]
lista = [random.randint(1, 10000000) for _ in range(10000000)]

def sumas(inicio, fin):
    partial_sum = 0
    for i in range(inicio, fin):
        partial_sum += lista[i]
    total[0] += partial_sum
h1 = Thread(target=sumas, args=(0, 5000000))
h2 = Thread(target=sumas, args=(5000000, 10000000))
h1.start()
h2.start()

h1.join()
h2.join()
print("total:", total[0])

