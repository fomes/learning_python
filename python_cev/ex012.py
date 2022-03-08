# 012- Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input("Qual o preço do produto? R$: "))
novo_preco = preco - (preco*5/100)

print(f"Esse produto com 5% de desconto custará R$ {novo_preco}")
