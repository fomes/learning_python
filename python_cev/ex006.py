# 006- Solicite um número e retorne o dobro, triplo e raiz quadrada.

import math


num = int(input("Digite um número: "))

print("Dobro: ", num*2)
print("Triplo: ", num*3)
print("Raiz quadrada: %.2f" %math.sqrt(num)) # %.2f -> dois dígitos depois da vírgula
