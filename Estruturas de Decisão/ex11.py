n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if (n1 % 2 == 0) and (n2 % 2 == 0):
    print("Ambos os números são pares.")
else:
    print("Pelo menos um dos números é ímpar.")

if (n1 % n2 == 0):
    print(f"{n1} é divisível por {n2}.")
else:
    print(f"{n1} não é divisível por {n2}.")