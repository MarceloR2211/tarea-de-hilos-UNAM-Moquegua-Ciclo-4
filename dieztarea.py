""" 10. Ejercicio de Creación de Hilos Dinámicos: Suma de
 Matrices
 Enunciado: Implementa un programa en Python que realice la suma de dos
 matrices de 1000x1000 elementos utilizando hilos. Cada hilo debe calcular la
 suma de una fila de las matrices. Utiliza mecanismos de sincronización para
 combinar las filas sumadas en una matriz final.
 Pistas:
 • Divide las filas de las matrices entre los hilos.
 • Utiliza Thread y Lock para garantizar que las filas se sumen sin errores
"""
from threading import Thread, Lock
import random
lock=Lock()
matris1 = [[random.randint(1, 100) for _ in range(1000)] for _ in range(1000)]
matris2 = [[random.randint(1, 100) for _ in range(1000)] for _ in range(1000)]
matrissuma = [[0 for _ in range(1000)] for _ in range(1000)]

def sumas(fila):

    
    for i in range(0, 1000):
        partial_sum = matris1[fila][i] + matris2[fila][i]
        with lock:
            matrissuma[fila][i] = partial_sum

hilos = []
for i in range(1000):#aqui cambia cant de hilos
    hilo = Thread(target=sumas,args= (i,))
    hilos.append(hilo)
    hilo.start()


for hilo in hilos:
    hilo.join()

print("sumas:")
for fila in matrissuma:
    print(fila)
