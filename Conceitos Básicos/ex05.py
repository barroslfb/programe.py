"""Escreva um programa que receba a idade de uma pessoa em dias. 
Em seguida, converta essa idade para anos, meses e dias, e exiba o resultado. 
Para fazer essa conversão, assuma que um ano tem 365 dias e um mês tem 30 dias."""

idade = float(input("Digite sua idade em dias: "))
idade_anos = idade // 365
idade_meses = idade % 365 // 30
idade_dias = idade % 365 % 30

print(f"Você tem {idade_anos:.0f} anos, {idade_meses:.0f} meses e {idade_dias:.0f} dias.")