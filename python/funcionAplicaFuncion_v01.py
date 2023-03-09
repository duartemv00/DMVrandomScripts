# ENUNCIADO
# Escribir una función que reciba otra función y una lista, 
# y devuelva otra lista con el resultado de aplicar la función dada 
# a cada uno de los elementos de la lista.

def applyToAll(lt, fun):
    for i in lt:
        print(fun(i))

def elevarADos(i):
    return i*2

lt = [3,6,8,4,5]

#MAIN
applyToAll(lt,elevarADos)
