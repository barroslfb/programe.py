nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")
idade = int(input("Digite a idade: "))

if idade < 13:
    categoria = "infantil"
elif idade < 18:
    categoria = "juvenil"
elif idade < 36:
    categoria = "adulto"
else:
    categoria = "master"

print(f"O atleta {nome} {sobrenome} está na categoria {categoria}.")