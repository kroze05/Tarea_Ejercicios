# EJERCICIO 9.-  Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
meses = {"1":31,"2":27,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
llave = input("inserte un numero del uno al doce\n")
print(f"el numero de dias es:{meses[llave]}")