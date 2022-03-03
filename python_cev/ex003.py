# 003- Crie um programa que receba dois números e faça operações matemáticas

def calculator():
    num1 = int(input("Digite número 1: "))
    num2 = int(input("Digite número 2: "))
    result = 0

    operation = input("Escolha uma operação(| + | - | * | / |): ")

    if (operation == "+"):
        result = num1+num2

    elif(operation == "-"):
        result = num1-num2
    
    elif(operation == "*"):
        result = num1*num2

    elif(operation == "/"):
        result = num1/num2

    return f"Resultado: {result}"

print(calculator())
