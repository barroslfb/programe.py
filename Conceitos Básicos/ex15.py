"""Escreva um programa que permute(troque) o valor de duas variáveis inteiras. 
DICA: use uma terceira variável para armazenar temporariamente o valor a ser trocado."""

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
temp = a

a = b
b = temp

print(f"Valor de a após a troca é {a}")
print(f"Valor de b após a troca é {b}")