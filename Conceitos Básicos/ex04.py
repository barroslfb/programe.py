"""Escreva um programa que receba o 
nome de uma pessoa e sua idade em anos. 
O programa deve calcular e exibir a idade 
da pessoa em meses e dias, considerando 
que um ano tem 12 meses e um mês tem 30 dias."""

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

print(f"Sua idade em meses é {idade*12}.")
print(f"Sua idade em dias é {idade*365}.")