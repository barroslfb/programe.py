"""Escreva um programa que leia o salário de uma pessoa, 
quantas horas ela trabalha por dia e quantos dias ela trabalhou no mês. 
Em seguida, calcule e exiba quanto essa pessoa recebe por hora."""

salario = float(input("Digite seu salário: "))
horas = float(input("Digite quantas horas você trabalha por dia: "))
dias = float(input("Digite quantos dias você trabalha no mês: "))
valor_hora = salario/(dias*horas)

print(f"Você ganha {valor_hora} reais por hora de trabalho.")