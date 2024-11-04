"""Considerando que em um show: 
1) 45% dos ingressos vendidos foram meia-entrada; 
2) 55% dos ingressos vendidos foram inteiros; 
3)O valor do ingresso inteiro custava R$123,45 e 
4) o total de ingressos vendidos foi 6.789. 
Escreva um programa que calcule e exiba:
1. A quantidade de ingressos meia-entrada e inteira vendidos.
2. O valor faturado com cada tipo de ingresso.
3. O valor total faturado."""

ingresso = 6789
meia = ingresso*0.45
inteira = ingresso - meia

print(f"Foram vendidos {meia} ingressos meia-entrada e {inteira} ingressos inteira.")
print(f"Foi faturado {meia*123.45/2:.2f} reais nos ingressos meia-entrada e {inteira*123.45:.2f} reais nos ingressos inteira.")
print(f"O valor total faturado foi de {meia*123.45/2 + inteira*123.45:.2f} reais.")