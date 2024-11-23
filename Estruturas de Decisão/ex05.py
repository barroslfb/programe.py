n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação: ")

if operacao == '+':
    print(n1+n2)
elif operacao == '-':
    print(n1-n2)
elif operacao == '*':
    print(n1*n2)
elif operacao == '/':
    if n2==0:
        print("Impossível dividir por zero.")
    else:
        print(n1/n2)
else:
    print("Operação inválida.")