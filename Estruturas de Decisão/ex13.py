pares_positivos = []
pares_negativos = []
impares_positivos = []
impares_negativos = []
zero = []

for i in range(4):
    n = int(input(f"Digite o {i+1}° número: "))
    if n % 2 == 0:
        if n > 0:
            pares_positivos.append(n)
        elif n < 0:
            pares_negativos.append(n)
        else:
            zero.append(n)
    else:
        if n > 0:
            impares_positivos.append(n)
        else:
            impares_negativos.append(n)

for i in pares_positivos:
    print(i)

for i in pares_negativos:
    print(i)

for i in impares_positivos:
    print(i)

for i in impares_negativos:
    print(i)

for i in zero:
    print(i)