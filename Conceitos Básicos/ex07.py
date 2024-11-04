"""Escreva um programa que, leia um valor de custo 
e o percentual de lucro desejado, e na sequencia 
mostre o valor final do produto;"""

custo = float(input("Digite o valor: "))
percentual = float(input("Digite o percentual de lucro desejado: ")) / 100
valor = custo + custo*percentual

print(f"O valor final do produto é {valor}.")