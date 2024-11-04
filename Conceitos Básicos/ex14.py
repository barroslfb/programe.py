"""Escreva um programa para gerar o invertido de um número com três algarismos
(exemplo: o invertido de 123 é 321). 
Dicas: 
1) a unidade de um número é calculada assim: unidade = numero % 10; 
2) a dezena de um número é calculada assim: 
        dezena = (numero // 10) % 10 e 3) 
    a centena de um número é calculada assim: 
        centena = numero // 100, onde: // retorna o quociente (resultado) de uma divisão inteira e % retorna o resto de uma divisão inteira. """

numero = 123
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100
invertido = unidade*100 + dezena*10 + centena

print(f"Número invertido: {invertido}")