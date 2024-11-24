primeiro = int(input("Digite o primeiro número da sequência: "))
ultimo = int(input("Digite o último número da sequência: "))
qtd = ultimo - primeiro + 1
pares = 0
impares = 0


for i in range(primeiro, ultimo + 1):
    if i % 2 == 0:
        pares+=1
    else:
        impares+=1

print(f"Quantidade de número da sequência: {qtd}")
print(f"Quantidade de números pares da sequência: {pares}")
print(f"Quantidade de números ímpares da sequência: {impares}")