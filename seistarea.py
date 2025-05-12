"""
 6. Ejercicio de Bloqueo: Actualización de un Contador
 Global
 Enunciado: Crea un programa en Python que utilice 100 hilos para incre
mentar un contador global 10,000 veces. Asegúrate de utilizar un mecanismo
 de sincronización para evitar condiciones de carrera.
 Pistas:
 • Utiliza Thread y Lock para asegurar que el contador se actualice de
 manera segura.
 • Cada hilo debe incrementar el contador en 100 veces
"""
from threading import Thread, Lock

contador = [0]
lock = Lock()

def incrementar():
    for _ in range(100):
        with lock:
            contador[0] += 1

hilos = [Thread(target=incrementar) for _ in range(100)]
for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Valor final del contador:", contador)
