#Desafio 96
'''L = C = 0
def area(L, C):
    print('CONTROLE DE TERRENO')
    print('━' * len('CONTROLE DE TERRENO'))
    L = float(input('Largura(m): '))
    C = float(input('Comprimento(m): '))
    print(f'A área de um terreno {L}x{C} é: {L * C}m².')

area(L, C)'''

#Desafio 97
'''def escreva(msg):
    tam = len(msg)
    print('━' * tam)
    print(msg)
    print('━' * tam)


escreva('GYM')
escreva('POWER')
escreva('OF')
escreva('GOD')'''

#Desafio 98
'''from time import sleep
def contagem(inicio, fim, passo):
    fim += 1
    print('━' * 40)
    print(f'Contagem de {inicio} até {fim-1} de {passo} em {passo}')
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.3)

    if inicio > fim:
        for e in range(inicio, fim, passo):
            print(e, end=' ')
    print()


contagem(1, 10, 1)
contagem(10, 0, 2)'''

#Desafio  99
'''def maior(*num):
    if len(num) == 0:
        print('Não encontrei elementos.')
    else:
        print(f'Em {num} existe {len(num)} elementos, o maior valor é {max(num)}.')


maior(4, 7, 8, 6, 3)
maior(3, 4, 9, 1)
maior(5, 6)
maior(0)
'''


#Desafio 100
'''from random import randint
num = []
pares = []
def sortear():
    for c in range(0, 5):
        num.append(randint(0, 10))
    print(f'Os números sorteados foram: {num}')


def somapar():
    for c in range(0, 5):
        if num[c] % 2 == 0:
            pares.append(num[c])
    print(f'A soma dos números pares é: {sum(pares)}')

sortear()
somapar()'''
