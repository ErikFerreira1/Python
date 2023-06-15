#Desafio 46
from time import sleep
import random
'''print('CONTAGEM DE FOGOS DE ARTIFICIO!\nCOMO EM:')
Cores = '\033[31m', '\033[32m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[94m'
for c in range(10, 0, -1):
    print(Cores[random.randint(0, 6)] + str(c))
    sleep(1)'''

#Desafio 47
'''for c in range(0, 51, 2):
    print(c)'''

#Desafio 48
'''n = 0
for c in range(3, 501, 6):
    if c % 2 == 0:
        print()

    elif c % 2 == 1:
        print(c)
        n += c
        print(f'A soma é: {n}')'''

#Desafio 49
'''Num = int(input('Digite um número:'))
for c in range(1, 11):
    print(f'{Num} x {c} = {Num * c}')'''

#Desafio 50
'''n = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        n += 1
        cont = cont + 1
print(f'A soma dos números foi {n} e a contagem foi {cont}')'''

#Desafio 51
'''A = int(input('Digite o primeiro termo: '))
B = int(input('Digite a razão: '))
for c in range(A, (A +10*B), B):
    print(c, end=' ')'''

#Desafio 52
Num = int(input('Digite um número para saber se ele é primo: '))
for primo in range(1, Num+1):
    if Num % primo == 0:
        print('\033[34m', end= " ")
    else:
        print('\033[31m', end=' ')
    print(f'{primo}', end=' ')

#Desafio 53
'''frase = str(input('Digite uma frase: ')).upper().strip()
txt = frase[::-1]
A = txt.find(frase)
if A == 0:
    print('A frase é polindrona')
else:
    print('A frase não é polindrona')'''

#Desafio 54
'''n = 0
for nome in range(1, 4):
   ano =  int(input(f'Digite o ano de nascimento do {nome}º nome: '))
   idade = 2023 - ano
   if idade <= 17:
      n += 1
print(f'menores são: {n}')
print(f'maiores são: {3-n}')'''

#Desafio 55
'''a = cont = 0
maior = menor = 0
for c in range(1, 4):
    a = float(input(f'Digite o peso da {c}º pessoa: '))
    cont += a
    if c == 1:
        maior = menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
print(f'maior peso é {maior} e o menor é {menor}.')'''

#Desafio 56
'''for i in range (1, 5):
    nome = str(input(f'Digite o nome da {i}º pessoa: '))
    sexo = str(input(f'Digite o sexo da {i}º pessoa [M/F]: ')).upper()
    idade = int(input(f'Digite a idade da {i}º pessoa: '))
    cont += idade
    if sexo == 'M':
        if idade > idade_homem:
            idade_homem = idade
            nome_homem = nome
    if sexo == 'F':
        if idade < 20:
            mulheres += 1
print(f'A média de idade do grupo é {cont/4}.')
print(f'O nome do homem mais velho é {nome_homem} e a idade dele é {idade_homem}')
print(f'Exitem {mulheres} mulher abaixo de 20 anos')'''
































