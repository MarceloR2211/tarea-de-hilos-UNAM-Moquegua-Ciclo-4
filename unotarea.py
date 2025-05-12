"""
 1. Ejercicio Básico de Hilos: Suma de Números
 Enunciado: Escribe un programa en Python que utilice dos hilos para cal
cular la suma de los primeros 1,000,000 de números naturales. Cada hilo debe
 calcular la suma de la mitad de la lista, y el resultado debe ser combinado
 al final. Utiliza un mecanismo de sincronización para evitar condiciones de
 carrera.
 Pistas:
 • Usa la librería threading.
 • Utiliza Thread para crear los hilos.
 • Implementa Lock para sincronizar el acceso a la variable compartida
"""
"""# Importar módulos necesarios
import math
import time
from threading import Thread, Lock
from multiprocessing import Process, Manager

manager = Manager()
Lock=Lock()

mitad_uno=manager.Value(i,0)
mitad_dos=0

def suma_mitad(a):
    with lock:  
        for i in range(0 , 5000001):
            a+=i
        return a

def suma_otra_mitad(a):

    with lock:  
        for i in range(500000, 1000001):
             a+=i
        return a

h1=Process(target=suma_mitad, args=(mitad_uno))
h2=Process(target=suma_mitad, args=(mitad_uno))
h1.start()
h2.start()
h1.join()
h2.join()
total= mitad_uno + mitad_dos
print("total",total )
"""
from threading import Thread, Lock
lock=Lock()

total = [0]


def sumas( inicio, fin):

    partial_sum = 0
    for i in range(inicio, fin):
        partial_sum += i
    with lock:
        total[0] += partial_sum
    

h1=Thread(target=sumas, args=(1,500001))
h2=Thread(target=sumas, args=(500001,1000001))
h1.start()
h2.start()
h1.join()
h2.join()
print("total:", total[0])
