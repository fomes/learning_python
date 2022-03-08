# Crie um programa que receba o valor em real e converta para dolar

valor_real = float(input("Digite valor em real: "))
cotacao_dolar = float(input("Digite valor da cotação do dolar: "))
valor_dolar = valor_real/cotacao_dolar

print(f"Valor em dólar: {valor_dolar} USD")
