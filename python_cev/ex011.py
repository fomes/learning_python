# 011- Faça um programa que leia a largura e altura de uma parede em metros, calcule sua area e a quatidade necessária de tinta para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura*altura
tinta = area/2

print(f"Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m²")
print(f"Para pintar essa parede é necessaário {tinta}L de tinta")