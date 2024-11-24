pares = []
impares = []

for i in range(3):
    n = int(input(f"Digite o {i+1}° número: "))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

for j in pares:
    print(j)

for k in impares:
    print(k)