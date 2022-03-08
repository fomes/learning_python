# 008- Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

unidade_m = float(input("Digite um valor em metros: "))
unidade_cm = unidade_m*100
unidade_mm = unidade_m*1000

print(f"Valor em centímetros: {unidade_cm}")
print(f"Valor em milímetros: {unidade_mm}")
