# EJERCICIO 12.- Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.
val = input("inserte una letra\n")
mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
if val in mayusculas:
    print("la letra introducida es mayúscula")
else:
    print("la letra introducida es minúscula")