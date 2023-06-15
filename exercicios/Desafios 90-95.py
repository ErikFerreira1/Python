#Desafio 90
'''situa = {}
situa['nome'] = str(input('Digite o nome do aluno: ')).capitalize()
situa['media'] = float(input(f'Digite a media de {situa["nome"]}: '))
print(f'O nome do aluno é {situa["nome"]} sua média é {situa["media"]}\nSituação: ', end='')
if situa['media'] >= 7:
    print('Aprovado')
else:
    print('Reprovado')
print()'''

#Desafio 91
'''from random import randint

game = {}
cont = 1
game['jogador1'] = randint(1, 6)
game['jogador2'] = randint(1, 6)
game['jogador3'] = randint(1, 6)
game['jogador4'] = randint(1, 6)

for k, v in game.items():
    print(f'O {k} tirou {v}')
print('-=' * 30)
for i in sorted(game, key=game.get, reverse=True):
    print(f'{cont}º lugar: {i} com {game[i]}')
    cont += 1'''

#Desafio 92
'''dados = {}

dados['nome'] = input('Nome: ').strip().capitalize()
dados['idade'] = int(input('Ano de nascimento: '))
dados['idade'] = 2023 - dados['idade']
dados['carteira'] = int(input('CTPS: '))

if dados['carteira'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['contratação'] + 30 - 2023 + dados['idade']
    dados['salário'] = float(input('Salário: R$ '))

    print('━' * 27)
    for k, v in dados.items():
        print(f'{k}: {v}')
    print('━' * 27)
else:
    print('━' * 27)
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {dados["idade"]}')
    print('━' * 27)'''

#Desafio 93
'''jogador = {}
list_jogador = []
quant_gols = []
while True:
    list_jogador.append(jogador.copy())
    jogador['nome'] = str(input('Digite o nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou:  '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c+1}? '))
        quant_gols.append(gols)
        jogador['gols'] = quant_gols
    resp = str(input('Quer continuar? S/N')).upper()
    if resp != 'S':
        break
jogador['total'] = sum(quant_gols)
print('━' * 40)
print(jogador)
print('━' * 40)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('━' * 40)
print(f'O jogador {jogador["nome"]}, jogou {partidas}.')
for c in range(0, partidas):
    print(f'Na partida {c+1}, fez {quant_gols[c]} gols.')
print(f'Total de gols foi: {sum(quant_gols)}')
'''
#Desafio 94
'''dados = {}
list_dados = []
mulheres = []
media = soma = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).capitalize().strip()
    while True:
        dados['Sexo'] = str(input('Sexo M/F: ')).upper()
        if dados['Sexo'] in 'MF':
            break
            print('Digito incorreto! Digite novamente.')
        dados['idade'] = int(input('Idade: '))
        soma += dados['idade']
        list_dados.append(dados.copy())
        while True:
            resp = str(input('Quer continuar? S/N ')).upper()[0]
            if resp in 'S':
                break
            print('Digito incorreto! Digite novamente')
        if resp == 'N':
            break
print()
print(f'A média de idade do grupo é: {media}')
print(f'')
print(f'Mulheres cadastradas: {mulheres}')'''









