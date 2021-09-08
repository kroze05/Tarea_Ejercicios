# EJERCICIO 7.- Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero.
val_1 = int(input("inserte un numero\n"))
val_2 = int(input("inserte otro numero\n"))
val_op = val_1 + val_2
if val_op > 0:
    print("resultado positivio")
if val_op < 0:
    print("resultado negativo")
if val_op == 0:
    print("resultado cero")
    