#Desafio 101
'''def voto(ano=0):
    idade = 2023 - ano
    if idade >= 18 and idade < 71:
        print(f'{idade} anos, voto obrigatorio.')
    elif idade > 70 or idade == 16 or idade == 17:
        print(f'{idade} anos, voto não é obrigatorio.')
    else:
        print(f'{idade} anos, não vota.')
    return idade
n = int(input('Digite o ano de nascimento: '))
voto(n)'''

#Desafio 102
'''def fatorial(num, show=False):
    n = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' * ', end='')
            else:
                print(' = ', end='')
        n *= c
    return n



print('Coloque ápos o número: show=True. Para ver o calculo')
print(fatorial(5, show=False))'''

#Desafio 103
'''def ficha(nome, gols):
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} marcou {gols} gols.')

jogador = str(input('Digite o nome do jogador: '))
gol = str(input('Digite a quatidade de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
ficha(jogador, gol)'''

#Desafio 104
'''def leiaint():
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Digite um número valido.')
    print(f'Você digitou o número: {num}')

n = leiaint()'''

#Desafio 105
'''def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adiconar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    D = dict()
    D['total'] = len(num)
    D['maximo'] = max(num)
    D['minimo'] = min(num)
    D['média'] = sum(num) / len(num)
    if sit:
        if D['média'] >= 7:
            D['Situação'] = 'Boa'
        elif D['média'] >= 5:
            D['Situação'] = 'Razoável'
        else:
            D['Situação'] = 'Ruim'
    return D


resp = notas(8, 3, 5)
help(notas)
print(resp)'''

#Desafio 106
def linhas(msg):
    print('━' * len(msg))
linhas('SISTEMA DE AJUDA PYHELP ')
print('SISTEMA DE AJUDA PYHELP')
linhas('SISTEMA DE AJUDA PYHELP ')
while True:
    i = str(input('Função ou biblioteca > '))
    if i == 'FIM':
        print('PROGRAMA ENCERRANDO')
        break
    ajuda = help(i)






