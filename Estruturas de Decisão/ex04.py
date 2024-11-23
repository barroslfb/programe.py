caractere = input()

if (caractere == 'a') or (caractere == 'e') or (caractere == 'i') or (caractere == 'o') or (caractere == 'u'):
    print("O caractere digitado é uma vogal.")
elif (caractere >= '0') and (caractere <= '9'):
    print("O caractere digitado é um número.")
elif (caractere == '+') or (caractere == '-') or (caractere == '*') or (caractere == '/'):
    print("O caractere digitado é uma operação matemática.")
else:
    print("O caractere não é uma vogal, um número ou uma operação matemática.")