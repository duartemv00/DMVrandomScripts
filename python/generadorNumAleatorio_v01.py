# GENERADOR DE NÚMEROS PSEUDOALEATORIOS - Enunciado
# Crea un generador de números pseudoaleatorios entre 0 y 100.
# - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
# Es más complicado de lo que parece...

#EJERCICIO:
import time
from datetime import datetime

def generator01(): #using a set. No library needed
    numbers = {"0"}
    for x in range(100): numbers.add(str(x+1))
    for i in numbers: 
        print(int(i))
        break

def generator02(): #usando este método NO podemos llegar a obtner un 100
    print(datetime.now().microsecond%101)

#TEST
generator01()
generator02()
