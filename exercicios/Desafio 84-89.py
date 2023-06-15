#Desafio 84
'''dados = []
copia = []
cont = maior = menor = 0
while True:
    copia.append(str(input('Nome: ')))
    copia.append(int(input('Peso: ')))
    dados.append(copia[:])
    copia.clear()
    resp = str(input('Continuar? S/N ')).upper().strip()
    cont += 1
    if resp != 'S':
        break
    for p in dados:
        if cont == 1:
            maior = menor = p[1]
        if p[1] >= maior:
            maior = p[1]
        if p[1] <= menor:
            menor = p[1]

print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi {maior} kg, e foi alcançado por: ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi {menor} kg, e foi alcançado por: ', end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
'''

#Desafio 85
'''num = [[], []]
valor = 0
for i in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
        num[0].sort()
    else:
        num[1].append(valor)
        num[1].sort()
print(num[0], num[1])'''

#Desafio 86,87
'''matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
pares = []
for c in range(0, 3):
    for p in range(0, 3):
        valor = int(input('Digite um valor: '))
        matriz[c][p] = valor
        if valor % 2 == 0:
            pares.append(valor)
print('-='*30)
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[c][p]:^5}]', end=' ')
    print()
print('-='*30)
print('A soma de todos valores pares é:', sum(pares))
print('A soma dos valores da última coluna é:', matriz[0][2] + matriz[1][2] + matriz[2][2])
print('O maior valor na segunda linha é:', max(matriz[2]))
'''

#Desafio 88
'''from random import randint
copia = []
resp = int(input('Quantidade de jogos para sortear: '))
for _ in range(0, resp):
    num = [[], [], [], [], [], []]
    for c in range(0, 6):
        n = randint(1, 60)
        num[c].append(n)

    for d in range(0, 6):
        a = num.count(num[d])
        if a > 1:
            num[d] = [randint(1, 60)]
            for d in range(0, 6):
                a = num.count(num[d])
                if a > 1:
                    num[d] = [randint(1, 60)]
    print(f'Seus números são: {num}')
    num.clear()'''

#Desafio 89
'''lista = [[], [], []]
zona = []
cont = 0
while True:
    nome = str(input('Digite o nome: '))
    lista[0].append(nome)
    nota = float(input('Digite a primeira nota: '))
    lista[1].append(nota)
    nota2 = float(input('Digite a segunda nota: '))
    lista[2].append(nota2)
    tabela = f'{nome: <15} {sum(lista[1] + lista[2]) / 2: ^5}'
    zona.append(tabela)
    for c in range(0, 3):
        lista[c].clear()
    resp = str(input('Quer continuar? S/N')).upper().strip()
    cont += 1
    if resp != 'S':
        break
print('━' * 27)
str(print('Num', 'Nomes'.rjust(6), 'Notas'.rjust(15)))
print('━'*27)
for a in range(0, cont):
    print(f'{a:<5}{zona[a]}')
'''





