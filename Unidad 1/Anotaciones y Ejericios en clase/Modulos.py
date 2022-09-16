import random
from Operaciones import suma,resta
numRandom = random.randint(1,100)

while True:
    numero = int(input("Adivina el numero entre 1 y 100"))

    if(numero == numRandom):
        break
    if(numero>numRandom):
        print("El numero es menor")
    else:
        print("El numero es mayor")

print("El numero es: "(numRandom))

print(suma(1,5))