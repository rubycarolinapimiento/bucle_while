# blucle while

import math

numero=int(input("ingrese un numero: "))

while numero<0:
    print("ERROR -> EL NUMERO DEBE SER POSITIVO")
    numero=int(input("ingrese un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")
