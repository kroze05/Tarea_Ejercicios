# EJERCICIO 8.-  Escribe un programa que lea un número e indique si es par o impar
val = int(input("coloque un numero\n"))
val %= 2
if val == 1:
    print("el resultado es impar")
else:
    print("el resultado es par")