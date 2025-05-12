""" 8. Ejercicio de Sincronización Avanzada: Fila de Tareas
 Enunciado: Implementa un programa en Python donde varios hilos procesen
 tareas de una cola compartida. Cada hilo debe tomar una tarea de la
 cola y procesarla. Utiliza Queue de Python para manejar la cola y Lock para
 asegurar que los hilos no accedan simultáneamente a las tareas.
 Pistas:
 • Utiliza Queue para manejar las tareas.
 • Usa Thread para los hilos y Lock para sincronización"""
from threading import Thread, Lock
from queue import Queue
import random

tareas = Queue()
lock = Lock()


for i in range(20):
    tareas.put(f"Tarea {i+random.randint(1, 100)}")

def trabajador():
    while not tareas.empty():
        with lock:
            if not tareas.empty():
                tarea = tareas.get()
                print(f"{Thread.current_thread().name} procesando {tarea}")
        


hilos = []
for i in range(5):#aqui cambia cant de hilos
    hilo = Thread(target=trabajador, name=f"Hilo-{i+1}")
    hilos.append(hilo)
    hilo.start()


for hilo in hilos:
    hilo.join()

print("completado")