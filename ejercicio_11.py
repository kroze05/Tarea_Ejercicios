# EJERCICIO 11.-Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
ano=int(input("introduzca el año a comprobar\n"))
comp_1=ano / 4

if isinstance(comp_1,int) :
    print("el año si es bisiesto")
else:
    print("el año introducido no es bisiesto")