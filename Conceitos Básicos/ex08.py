"""Escreva um programa que, leia um valor de venda e um percentual de desconto,
 e depois apresente o valor a ser pago pelo produto e o valor do desconto que foi concedido;"""

venda = float(input("Digite o valor de venda: "))
percentual = float(input("Digite o percentual de desconto: ")) / 100
valor = venda * (1 - percentual)
desconto = venda*percentual

print(f"O valor a ser pago é {valor} reais e o desconto foi de {desconto} reais.")