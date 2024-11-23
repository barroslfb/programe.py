descricao = input("Descrição do produto: ")
tipo = input("Tipo do produto: ")
valor = float(input("Valor do produto: "))

if tipo == 'A' or tipo == 'B':
    reajuste = valor*0.123
elif tipo == 'C':
    reajuste = valor*0.14
elif tipo == 'D' or 'E':
    reajuste = valor*0.157
else:
    print("Erro: o tipo digitado é inválido.")
    reajuste = -1

if reajuste != -1:
    valor_reajustado = valor + reajuste

    print(f"Descrição do produto: {descricao}")
    print(f"Valor do produto: R${valor:.2f}")
    print(f"Valor do reajuste: R${reajuste:.2f}")
    print(f"Valor reajustado: R${valor_reajustado:.2f}")