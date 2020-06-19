def max():
    num1 = input("Escribe el primer número: ")
    num2 = input("\nEscribe el segundo número: ")
    if num1>num2:
        print(f"El numero mayor es el {num1}")
    elif num2>num1:
        print(f"El numero mayor es el {num2}")
    else:
        print("Los dos numeros son iguales")


max()
