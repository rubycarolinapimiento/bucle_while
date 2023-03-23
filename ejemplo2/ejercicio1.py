# bucle while

i = 1

#while i<=10:
 #   print(i)
  #  i += 1

numero=int(input("ingrese un numero positivo: "))

while numero<0:
    print("ERROR -> este es un numero negativo prueba de nuevo")
    numero=int(input("ingrese un numero positivo: "))
print("el numero es: ",numero)