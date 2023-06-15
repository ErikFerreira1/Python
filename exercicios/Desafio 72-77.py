#Desafio 72
'''num = int(input('Digite um número de 0 à 10: '))
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
contagem_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
if num in numeros:
    print('Você digitou o número', contagem_ext[num])
else:
    while num not in numeros:
        num = int(input('digito incorreto, tente novamente. Digite um número de 0 à 10: '))
    print('Você digitou o número', contagem_ext[num])'''

#Desafio 73
'''camp_bras = ('flamengo', 'santos', 'palmeiras', 'grêmio',
            'atletico paranaense', 'são paulo',
            'internacional', 'corinthians', 'fortaleza',
            'goias', 'bahia', 'vasco', 'atletico', 'fluminense',
            'botafogo', 'ceara', 'cruzeiro', 'csa', 'chapecoense',
            'avai')

print('Os 5 primeiros colocados do campeonato brasileiro são:', camp_bras[:5])
print('Os 5 ultimos colocados são:', camp_bras[-4:])
print(sorted(camp_bras))
print('Chapecoense está na', camp_bras.index('chapecoense'), 'colocação')'''

#Desafio 74
'''import random
num = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),random.randint(0, 10), random.randint(0, 10)
tupla = (num)
valor_maximo = max(tupla)
valor_minimo = min(tupla)
print(f' Os números são: {tupla}\n '
      f'O número maior é: {valor_maximo}\n'
      f' O número menor é: {valor_minimo}\n')'''

#Desafio 75
'''Num1 = (int(input('Digite o um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')),
        int(input('Digite outro valor: ')))
print('O número 9 apareceu:', Num1.count(9), 'vezes')
if Num1 == 3:
    print('O número 3 está na posição:', Num1.index(3+1))
else:
    print('O número 3 não foi digitado')
print('Os números pares são:', end= ' ')
for n in Num1:
    if n % 2 == 0:
        print(n, end= ' ')'''

#Desafio 76
'''lista_produto = ('Lápis', 1, 'Caneta', 2, 'Mochila', 50, 'Puta', 250, 'Caderno', 20, 'arma', 450)
print('='*45)
print('LISTA DE COMPRAS'.center(45))
print('='*45)
for i, produto in enumerate(lista_produto):
    if i % 2 == 0:
        impar = lista_produto[i]
    else:
        par = lista_produto[i]
        print(f'{impar:.<36}','R$', f'{par:}')
print('='*45)'''

#Desafio 77
'''palavras = ('gosto', 'cadeira', 'mouse', 'computador')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end= ' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end= '')'''



