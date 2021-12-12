# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.

# def bigger(num1, num2):
#   if num1 > num2:
#     return num1
#   else:
#     return num2

# print(bigger(10, 20))

# -------------------------------------------------------------------------------------------------------------------

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

# import statistics

# list_01 = [1, 2, 3]

# def med(list):
#   mean = statistics.mean(list)
#   return mean

# print(med(list_01))

# -------------------------------------------------------------------------------------------------------------------

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n . Por exemplo:

# n = 10

# for i in range(n):
#   print('* '*n)


# -------------------------------------------------------------------------------------------------------------------

# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" .
# Uma dica: Utilize a função len() para verificar o tamanho do nome.

# list_01 = ['felipe', 'gomes', 'luna']

# def biggerStr(listName):
#   return max(listName, key=len)

# print(biggerStr(list_01))

# -------------------------------------------------------------------------------------------------------------------

# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede(em m²).

# 1L = 3m²
# 1Lata = 18L = R$ 80,00

# import math

# def calcBuckets():
#   wall_size = input('Digite tamanho da parede: (m²): ')
#   wall_size = int(wall_size)
  
#   liters = wall_size/3
#   buckets = math.ceil(liters/18)
#   value = buckets*80

#   return str(buckets)+' lata(s)', 'R$ '+str(value)

# print(calcBuckets())


# -------------------------------------------------------------------------------------------------------------------

# Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo" , caso não seja possível formar um triângulo.
# Dica:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes.

# def eoTriangulas():
#   la = input('Digite tamanho do lado A: ')
#   lb = input('Digite tamanho do lado B: ')
#   lc = input('Digite tamanho do lado C: ')

#   la = int(la)
#   lb = int(lb)
#   lc = int(lc)

#   if(la==0 or lb==0 or lc==0):
#     return 'Nao é o triangulas!'
#   else:
#     if(la==lb==lc):
#       return 'Triângulo Equilátero!'
#     if(la==lb or la==lc or lb==lc):
#       return 'Triângulo Isósceles!'
#     if(la!=lb!=lc):
#       return 'Triângulo Escaleno!'

# print(eoTriangulas())
