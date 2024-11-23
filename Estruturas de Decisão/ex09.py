valor_diaria = float(input("Digite o valor da diária: "))
dias_faltou = int(input("Digite quantos dias faltou: "))
dias_presente = 26 - dias_faltou
salario_integral = valor_diaria*26

if dias_faltou == 0:
    bonus = salario_integral*0.123
    salario_bonificado = salario_integral + bonus
    print(f"Salário integral: R${salario_integral:.2f}")
    print(f"Bônus: R${bonus:.2f}")
    print(f"Salário bonificado: R${salario_bonificado:.2f}")
else:
    salario_desconto = valor_diaria*dias_presente
    print(f"Quantidade de faltas: {dias_faltou}")
    print(f"Salário com desconto: R${salario_desconto:.2f}")
    print(f"Salário integral: R${salario_integral:.2f}")
    print(f"Valor do desconto: R${salario_integral-salario_desconto:.2f}")
    print(f"Percentual do desconto: {100*(salario_integral-salario_desconto)/salario_integral:.2f}%")   
    