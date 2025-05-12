""" 2. Ejercicio de Sincronización: Contador de Primos
 Enunciado: Implementa un programa en Python con dos hilos. El primer
 hilo debe contar cuántos números primos hay en un rango de números, y el
 segundo hilo debe calcular la suma de todos esos números. Los dos hilos
 deben acceder a una lista compartida que contiene los números. Asegúrate
 de utilizar mecanismos de sincronización.
 Pistas:
 • Usa Lock para proteger las operaciones sobre la lista compartida.
 • Implementa una función para verificar si un número es primo."""
"""
from threading import Thread, Lock
lock=Lock()

print("de un rango")
inicio=input("inngrese inicio")
fin=input("ingrese fin")

def cantidad_primos (lista):
    esprimo = True  
    for j in range(2, int(i ** 0.5) + 1):
        if lista[j] % j == 0:
            esprimo = False
            break 
    if (esprimo==True):
        datos[0] += 1

def suma_primos (lista):
    esprimo = True  
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            esprimo = False
            break 
    if (esprimo==True):
        datos[1] += lista[j]

if (inicio>=fin):
    print("error")
else:
    lista = []
    for i in range(inicio, fin+1):
        lista.append(i)
    datos=[0,0]

    h1=Thread(target=cantidad_primos, args=(inicio,fin))
    h2=Thread(target=suma_primos, args=(inicio,fin))
    h1.start()
    h2.start()
    h1.join()
    h2.join()
    print("cantidad:", lista[0])
    print("suma:", lista[1])
"""
from threading import Thread, Lock

lock = Lock()
datos = [0, 0]
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def cantidad_primos(lista):
    global datos
    for num in lista:
        if es_primo(num):
            with lock:
                datos[0] += 1

def suma_primos(lista):
    global datos
    for num in lista:
        if es_primo(num):
            with lock:
                datos[1] += num

inicio = int(input("ingrese inicio: "))
fin = int(input("ingrese fin: "))

if inicio >= fin:
    print("error")
else:
    lista = list(range(inicio, fin + 1))

    h1 = Thread(target=cantidad_primos, args=(lista,))
    h2 = Thread(target=suma_primos, args=(lista,))

    h1.start()
    h2.start()
    h1.join()
    h2.join()

    print("cantidad:", datos[0])
    print("suma:", datos[1])

    
