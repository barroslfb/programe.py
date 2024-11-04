"""Escreva um programa que, a partir de um valor de custo 
e de um valor de venda, mostre o valor do lucro obtido 
com a venda do produto;"""

custo = float(input("Digite o valor de custo: "))
venda = float(input("Digite o valor da venda: "))
lucro = venda - custo

print(f"O valor do lucro é {lucro}.")