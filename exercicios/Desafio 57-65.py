#Desafio 57
'''M = 'M', 'F'
Sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while Sexo != 'M' and Sexo != 'F':
     A = input('Sexo invalido, digite novamente! [M/F]: ').upper()
     if A == 'M' or A == 'F':
          break
print('Fim')'''

#Desafio 58
'''import random
A = 1
Num = random.randint(1, 10)
print(Num)
print('=-'*20, 'JOGO DA ADIVINHA', '=-'*20)
Escolha = int(input('ESCOLHA UM NÚMERO DE 1 A 10: '))
if Escolha == Num:
     print('PARABÉNS! VOCÊ ACERTOU!\nA QUANTIDADE DE TENTATIVAS FOI: 1')
while Escolha != Num:
     Escolha = int(input('VOCÊ ERROU, TENTE NOVAMENTE. DIGITE OUTRO NÚMERO: '))
     A += 1
     if Escolha == Num:
          print('PARABÉNS! VOCÊ ACERTOU!')
          print(f'A QUANTIDADE DE TENTATIVAS FOI: {A}')
          break'''

#Desafio 59
'''Tabela = ""

Num1 = int(input('Digite o primeiro valor: '))
Num2 = int(input('Digite o segundo valor: '))
while Tabela != 5:
     print(          [1]Somar
          [2]Multiplicar
          [3]Maior
          [4]Novos Números
          [5]Sair do programa)
     Tabela = int(input('Escolha a opção: '))
     if Tabela == 1:
          Soma = Num1 + Num2
          print(f'A Soma entre {Num1} e {Num2} é {Soma} ')
     elif Tabela == 2:
          Mult = Num1 * Num2
          print(f'A multiplicação entre {Num1} e {Num2} é {Mult} ')
     elif Tabela == 3:
          if Num1 > Num2:
               print(f'{Num1} é maior que {Num2}')
          else:
               print(f'{Num2} é maior que {Num1}')
     elif Tabela == 4:
          Num1 = int(input('Digite o primeiro valor: '))
          Num2 = int(input('Digite o segundo valor: '))
     elif Tabela == 5:
          break
     else:
          print('OPÇÃO INVALIDA!')
          break'''

#Desafio 60
'''from math import factorial
f = 0
Num = int(input('Digite um valor: '))
while Num > 0:
    f = factorial(Num)
    print(f)
    break'''

#Desafio 61,62
'''Primeiro = int(input('Digite o primeiro termo: '))
Raz = int(input('Digite a razão: '))
termo = Primeiro
cont = 1
l = 0
mais = 10
while mais != 0:
    l = l + mais
    while cont <= l:
        print(f'{termo}', end=' ')
        termo += Raz
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mais? '))
print('Fim')'''

#Desafio 63
'''t1 = 0
t2 = 1
n = int(input('Digite quantos termos: '))
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3, end= ' ')
    t1 = t2
    t2 = t3
    cont += 1
print(' ')'''

#Desafio 64
'''N = 0
cont = 0
resul = 0
while N != 999:
    N = int(input('Digite um valor: '))
    resul += N
    cont += 1
print(f'Você digitou {cont-1} numeros, a soma entre eles foi {resul - 999}')'''

#Desafio 65
'''media = maior = menor = n = cont = 0
af = 'S'

while af == 'S':
    n = int(input('Digite um número: '))
    af = str(input('Quer continuar? [S/N]')).upper()
    cont += 1
    media += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'o maior número é {maior}, o menor numero é {menor}, a media entre todos os números é {media/cont}')'''
while True:
    cont = 0
    num = int(input('Digite um número: '))
    if num < 0:
        break
    while cont <= 9:
        cont += 1
        print(num*cont)








































