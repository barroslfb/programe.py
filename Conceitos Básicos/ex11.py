"""Crie um programa que receba uma temperatura em Celsius e, 
considerando as seguintes fórmulas K=C+273 e F=1,8C+32, 
exiba a temperatura lida usando as escalas Kelvin (K) e Fahrenheit (F)."""

celsius = float(input("Digite a temperatura em graus celsius: "))
kelvin = celsius + 273
fahre = 1.8*celsius + 32

print(f"{kelvin} K")
print(f"{fahre}° F")