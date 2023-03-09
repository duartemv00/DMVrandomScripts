# Escribir una función que reciba otra función booleana y una lista, 
# y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

def applyToAll(lt, fun):
    for i in lt:
        fun(i)

def ifEvenReturnTrue(i):
    if i%2 == 0:
        print("Even")

lt = [1,2,3,4,5]
applyToAll(lt,ifEvenReturnTrue)