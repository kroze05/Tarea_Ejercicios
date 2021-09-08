#EJERCICIO 15.- Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.
val=int(input("inserte el numero a adivinar\n"))
print("pasalo a la persona que deseas que adivine\n")
num_in=int(input("adivina el numero\n"))
while num_in != val:
    if num_in > val:
        num_in=int(input("el numero ingresado es mayor al que quieres adivinar, coloca otro numero\n"))
    elif num_in < val:
        num_in=int(input("el numero ingresado es menor al que quieres adivinar, coloca otro numero\n"))

print("el numero que colocaste es el correcto, felicidades")