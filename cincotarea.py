"""
5. Ejercicio Avanzado: Ordenamiento de una Lista con
 Hilos
 Enunciado: Implementa un programa en Python que utilice múltiples hilos
 para ordenar una lista de números. Cada hilo debe ordenar una sublista de
 números y luego combinar los resultados utilizando un algoritmo de fusión.
 Pistas:
 • Usa la función sorted() o merge sort.
 • Divide la lista en partes y asigna cada parte a un hilo.
 • Combina los resultados al final
"""
from threading import Thread, Lock
from functools import reduce
import random
lock=Lock()

tamano = int(input("ingrese el tamano de la lista: "))
total = [0]
lista = [random.randint(1, tamano) for _ in range(tamano)]

cant_hilos = int(input("ingrese el cantidad de hilos mas 5: "))

def dividir_lista(lista, n):
    k, m = divmod(len(lista), n)
    return [lista[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

def ordenar_sublista(idx, sublista, resultados):
    ordenada = sorted(sublista)
    with lock:
        resultados[idx] = ordenada

def fusionar(l1, l2):
    resultado = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            resultado.append(l1[i])
            i += 1
        else:
            resultado.append(l2[j])
            j += 1
    resultado.extend(l1[i:])
    resultado.extend(l2[j:])
    return resultado

sublistas = dividir_lista(lista, cant_hilos)
resultados = [None] * cant_hilos
hilos = []

for i in range(cant_hilos):
    t = Thread(target=ordenar_sublista, args=(i, sublistas[i], resultados))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()

lista_ordenada = reduce(fusionar, resultados)

print(lista_ordenada)