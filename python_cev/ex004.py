# 004- Solicite um valor qualquer int ou str e informe o tipo, se tem espaços, se é numérico, se é alfanumérico, se está em maiúsculo ou minúsculo.

var = input("Digite alguma coisa: ")

print("Qual o tipo primitivo? : ", type(var))
print("Só tem espaços? ", var.isspace())
print("É um número? ", var.isnumeric())
print("É alfabético? ", var.isalpha())
print("É alfanumérico? ", var.isalnum())
print("Está em maiúsculo? ", var.isupper())
print("Está em minúsculo? ", var.islower())
print("Está captalizada? ", var.istitle()) # Primeira letra maiúscula
