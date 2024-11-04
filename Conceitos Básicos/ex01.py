"""Escreva um programa que leia as 2 notas de um aluno
em uma disciplina, depois exiba quantos pontos o aluno
ficou distante da nota 10 para cada avaliação, 
sua média e quantos pontos a média do aluno
ficou distante da nota 10."""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2

print("Na primeira prova, você ficou ",10 - n1," pontos abaixo da nota 10.")
print("Na segunda prova, você ficou ",10 - n2," pontos abaixo da nota 10.")
print("Sua média ficou ",10 - media," pontos abaixo da média 10.")