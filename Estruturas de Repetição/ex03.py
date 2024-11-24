contador = 0

while True:
    continua = input("Deseja informar um novo número? (s/n): ")
    if continua == 'N':
        break
    else:
        numero = int(input("Digite um número inteiro e positivo: "))
        contador+=1

print(f"O total de números foi: {contador}")