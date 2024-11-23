media_salarial = float(input("Digite a média salarial: "))
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario < media_salarial:
    print(f"O salário de {nome} é menor que a média.")
elif salario > media_salarial:
    print(f"O salário de {nome} é maior que a média.")
else:
    print(f"O salário de {nome} é igual a média.")