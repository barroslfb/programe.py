"""Considerando que a altura de um prédio está para a 
altura de uma pessoa assim como a sombra de um prédio está para a 
sombra de uma pessoa (isto é, altura_predio/altura_pessoa = sombra_predio/sombra_pessoa), 
faça um programa para estimar a altura de um prédio, 
a partir da leitura da sombra do prédio, da sombra da pessoa e da altura da pessoa."""

sombra_predio = float(input("Digite a sombra do prédio: "))
sombra_pessoa = float(input("Digite a sombra da pessoa: "))
altura_pessoa = float(input("Digite a altura da pessoa: "))
altura_predio = sombra_predio*altura_pessoa/sombra_pessoa

print(f"A altura do prédio é {altura_predio:.2f}")