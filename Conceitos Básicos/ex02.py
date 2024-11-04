"""Escreva um programa que, 
dado um dos lados de um quadrado, 
exiba a sua área e o seu perímetro."""

lado = float(input("Digite o tamanho do lado do quadrado: "))
area = lado*lado
perimetro = lado*4

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")