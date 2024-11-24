numeros = []

for i in range(3):
    numeros.append((int(input(f"Digite o {i+1}° número: "))))

if (numeros[0] < numeros[1] + numeros[2]) and (numeros[1] < numeros[0] + numeros[2]) and (numeros[2] < numeros[0] + numeros[1]):
    print("Os segmentos formam um triângulo")
    if (numeros[0] == numeros[1]) and (numeros[1] == numeros[2]):
        print("O triângulo é equilátero.")
    elif (numeros[0] != numeros[1]) and (numeros[1] != numeros[2]) and (numeros[2] != numeros[0]):
        print("O triângulo é escaleno.")
    else:
        print("O triângulo é isósceles.")
else:
    print("Esses segmentos de reta não formam um triângulo.")