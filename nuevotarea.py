""" 9. Ejercicio de Programación en Memoria Compartida:
 Suma y Promedio en Paralelo
 Enunciado: Crea un programa en Python que calcule tanto la suma como
 el promedio de los elementos de una lista de números en paralelo utilizando
 dos hilos. Un hilo debe calcular la suma y el otro debe calcular el promedio.
 Pistas:
 • Calcula la suma en un hilo y el promedio en otro.
 • Utiliza Thread y un mecanismo de sincronización para manejar los
 resultados
"""
from threading import Thread, Lock
import random
lock=Lock()

tamano = int(input("ingrese el tamano de la lista: "))
total = [0,0]
lista = [random.randint(1, 100) for _ in range(tamano)]

def calcular_suma():
    suma_local = sum(lista)
    with lock:
        total[0] = suma_local

def calcular_promedio():
    promedio_local = sum(lista) / len(lista)
    with lock:
        total[1] = promedio_local
    

h1=Thread(target=calcular_suma)
h2=Thread(target=calcular_promedio)
h1.start()
h2.start()
h1.join()
h2.join()
print("suma:", total[0])
print("promedio:", total[0])