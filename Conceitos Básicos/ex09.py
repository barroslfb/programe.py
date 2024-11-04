"""Considerando que o valor do m² para concretar um piso é R$50. 
Escreva um programa que leia as medidas de um terreno retangular 
e informe quanto custa para concretá-lo por inteiro. """

valor = 50
comp = float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
area = comp*largura
custo = area*50

print(f"O custo para concretar o terreno foi de {custo} reais.")