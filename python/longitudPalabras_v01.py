# ENUNCIADO
# Escribir una función que reciba una frase y 
# devuelva un diccionario con las palabras que contiene y su longitud.

# PROBLEMAS A RESOLVER: Cuenta los símbolos de puntuación como letras

def seccionarPalabras(sentence):
    palabraDividida = {}
    word = ""
    for i in sentence:
        if i==" ":
            palabraDividida.update({word:len(word)})
            word = ""
        else:
            word = word + i
    palabraDividida.update({word:len(word)})
    return palabraDividida

sentence = str(input("Introduce una frase: "))


print(seccionarPalabras(sentence))