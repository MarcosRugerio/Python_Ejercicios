# '''
# Ejercicio 2
# Definir una función max_de_tres(), 
# que tome tres números como argumentos y
#  devuelva el mayor de ellos.
#'''
def max_de_tres(numero1,numero2,numero3):
    print("El número mayor es:") #Validand que se llame correctamente.
    if numero1 >= numero2:
        if numero1 >= numero3:
            numeroMayor = numero1
        else:
            numeroMayor = numero3
    else:
        if numero2 >= numero3:
            numeroMayor = numero2
        else:
            numeroMayor = numero3
    print(numeroMayor)

print("Este programa compara tres números y muestra el mayor de ellos\n")
numero1 = input ("\nEscribe tu primer número: ")
numero2 = input ("Escribe tu segundo número: ")
numero3 = input ("Escribe tu tercer número: ")

max_de_tres(numero1,numero2,numero3)