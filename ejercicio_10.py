# EJERCICIO 10.- Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “passwd#” se indica “Has entrado al sistema”, sino se da un error.
val = input("inserte el usuario\n")
if val == "pepe":
    con = input("inserte contraseña\n")
    if con == "passwd#":
        print("has entrado al sistema")
    else :
        print("error")
else:
    print("error")