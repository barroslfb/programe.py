numeros = []

for i in range(3):
    numeros.append((int(input(f"Digite o {i+1}° número: "))))

if numeros[0] <= numeros[1] and numeros[0] <= numeros[2]:
    if numeros[1] <= numeros[2]:
        print("Ordem crescente:", numeros[0], numeros[1], numeros[2])
    else:
        print("Ordem crescente:", numeros[0], numeros[2], numeros[1])
elif numeros[1] <= numeros[2]:
    if numeros[2] <= numeros[0]:
        print("Ordem crescente:", numeros[1], numeros[2], numeros[0])
    else:
        print("Ordem crescente:", numeros[1], numeros[0], numeros[2])
else:
    if numeros[0] <= numeros[1]:
        print("Ordem crescente:", numeros[2], numeros[0], numeros[1])
    else:
        print("Ordem crescente:", numeros[2], numeros[1], numeros[0])