# 009- Faça um progrma que leia um número inteiro e exiba sua tabuada na tela

num = int(input("Digite um número de 1 a 10 para ver sua tabuada: "))

print("------------------")
for i in range(10):
    print(f"{num} x {i+1} = {num*(i+1)}")

print("------------------")
