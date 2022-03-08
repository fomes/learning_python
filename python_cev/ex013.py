# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com aumento de 15%.

salario = float(input("Qual o sálario do funcionário R$: "))
novo_salario = salario + (salario*15/100)

print(f"Salario com 15 % de alumento será: R$ {novo_salario}")
