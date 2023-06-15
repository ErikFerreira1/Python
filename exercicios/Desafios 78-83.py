#Desafio 78

'''list = []
for n in range(5):
    num = int(input('Digite um valor: '))
    list.append(num)
menor = min(list)
maior = max(list)

print(f'OS NUMEROS DIGITADOS FORAM: {list}')
print(f'O MAIOR NÚMERO É: {maior} SUA POSIÇÃO É:', end=' ')
for pos, v in enumerate(list):
    if maior == v:
        print(pos, end=' ')
print(f'\nO MENOR NÚMERO É: {menor} SUA POSIÇÃO É:', end=' ')
for pos, v in enumerate(list):
    if menor == v:
        print(pos, end=' ')'''

#Desafio 79
'''lista = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if lista.count(num) == 1:
        print('Número adicionado!')
    if lista.count(num) > 1:
        print('Número já colocado. Será removido da lista')
        lista.pop()
    resp = str(input('Quer continuar? S/N ')).upper().strip()
    if resp != 'S':
        break
lista.sort()
print(lista)'''

#Desafio 80
'''lista = []
for i in range(5):
    num = int(input('Digite um valor: '))
    lista.append(num)
lista.sort()
print(lista)
'''
#Desafio 81
'''lista = []
while True:
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? S/N ')).upper().strip()
    lista.append(num)
    if resp != 'S':
        break
lista.sort(reverse=True)
print('Foram digitados:', len(lista), 'números')
print(f'A lista em ordem decrescente: {lista}')
if lista.count(5):
    print('O número 5 está na lista.', end=' ')
    for pos, v in enumerate(lista):
        if v == 5:
            print(f'E o 5 está na {pos}ª posição' )
else:
    print('O número 5 não está na lista')'''

#Desafio 82
'''lista = []
par = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = str(input('Quer continuar? S/N')).upper().strip()
    if resp != 'S':
        break
for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impares.append(numero)
print('Os números da lista são:', lista, 'Números pares:',  par,'Números impares:', impares)'''


