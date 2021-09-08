# EJERCICIO 5.-Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
val = int(input("ingrese la cantidad de minutos que desea convertir\n"))
val_int = val // 60
val_min = val % 60
print(f"su conversion en horas es: {val_int} y en minutos es: {val_min}")
