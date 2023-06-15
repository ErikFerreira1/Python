#Desafio 66
'''num = soma = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} e a soma entre eles é {soma}')'''

#Desafio 67
'''while True:
    i = 0
    num = int(input('Digite um número: '))
    if num < 0:
        break
    while i <= 9:
        i+=1
        print(i*num)'''

#Desafio 68
'''from random import randint
cont = 0
while True:
    comput = randint(1, 20)
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou impar [P/I]: ')).upper()
    pi = (comput + valor) % 2
    if pi == 0 and escolha == 'P':
        print(f'VOCÊ VENCEU!')
        
    if pi == 1 and escolha == 'I':
        print(f'VOCÊ VENCEU!')

    if pi == 1 and escolha == 'P':
        print(f'VOCÊ PERDEU!')
        break
    if pi == 0 and escolha == 'I':
        print(f'VOCÊ PERDEU!')
        break'''

#Desafio 69
'''cont_idade = idade_f = 0
cont_m = 0
while True:
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    idade = int(input('Digite sua idade: '))
    escolha = str(input('Você quer continuar? [S/N]')).upper().strip()
    if escolha == 'N':
        break
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_m = 1
        cont_m += 1
    if sexo == 'F' and idade < 20:
        idade_f += 1
print(f'pessoas maiores de 18: {cont_idade}, homens cadastrados {cont_m}, mulheres abaixo de 20 anos: {idade_f}')'''

#Desafio 70
'''soma = cont = cont2 = 0
menor = 0
nome_menor = ''
while True:
    nome_prod = str(input('Digite o nome do produto: ')).strip()
    preco_prod = float(input('Digite o valor do produto: '))
    rep = str(input('Continuar comprando? [S/N] ')).upper().strip()
    soma += preco_prod
    cont2 += 1
    if rep == 'N':
        break
    if preco_prod > 1000:
        cont += 1
    if cont2 == 1:
        menor = preco_prod
        nome_menor = nome_prod
        if preco_prod < menor:
            nome_menor = nome_prod
print(f'A soma de todos valores foi {soma}, {cont} custam mais de mil, o nome do produto mais barato é {nome_menor}')'''

#Desafio 71
'''print('=='*20)
str(print('\033[34mCAIXA ELETRONICO\033[m'.center(49)))
print('=='*20)
valor = int(input('Valor do saque: '))
print('Notas disponiveis: R$50, R$20, R$10, R$1')
ced_50 = ced_20 = ced_10 = ced_1 = 0
while valor > 0:
    if valor >= 50:
        ced_50 += 1
        valor -= 50
    elif valor >= 20:
        ced_20 += 1
        valor -= 20
    elif valor >= 10:
        ced_10 += 1
        valor -= 10
    elif valor >= 1:
        ced_1 += 1
        valor -= 1
    else:
        break
print(f' notas de 50: {ced_50}\n notas de 20: {ced_20}\n notas de 10: {ced_10}\n notas de 1: {ced_1}')'''

