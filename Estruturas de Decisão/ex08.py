valor_diaria = float(input("Digite o valor da diária: "))
dias = int(input("Digite a quantidade de dias que trabalhou no mês: "))
salario_bruto = valor_diaria*dias

if salario_bruto <= 2000:
    imposto = 0
elif salario_bruto <= 5000:
    imposto = salario_bruto*0.15
else:
    imposto = salario_bruto*0.275

salario_liquido = salario_bruto - imposto

print(f"O salário bruto é R${salario_bruto:.2f}, o Imposto de Renda a ser pago é de R${imposto:.2f} e o sálario líquido é de R${salario_liquido:.2f}.")