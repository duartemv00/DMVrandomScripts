# GENERADOR DE CONTRASEÑAS - Enunciado
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
#  - Longitud: Entre 8 y 16.
#  - Con o sin letras mayúsculas.
#  - Con o sin números.
#  - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

#EJERCICIO:
import random

optChar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
optCaps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
optNum = ["1","2","3","4","5","6","7","8","9","0"]
optSymb = ["?","¿","¡","!","·","#","~","$","%","€","&","¬","/","(",")"]

#Variables
passLen = 0
while (passLen < 8) or (passLen > 16): passLen = int(input("Introduce la longitud de la contraseña(8-16): "))
#¿Quieres mayúsculas?
answ = input("¿Quieres una contraseña con mayúsculas?(yes/no): ")
if answ.upper() == "YES": 
    for i in optCaps:
        optChar.append(i)
#¿Quieres números?
answ = input("¿Quieres una contraseña con números?(yes/no): ")
if answ.upper() == "YES": 
    for i in optNum:
        optChar.append(i)
#¿Quieres símbolos?
answ = input("¿Quieres una contraseña con símbolos?(yes/no): ")
if answ.upper() == "YES": 
    for i in optSymb:
        optChar.append(i)
#Bucle de creacion de la contraseña
while passLen != 0:
    passChar = random.choice(optChar)
    print(passChar,end="")
    passLen -= 1