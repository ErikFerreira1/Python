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
print(f'maior peso é {maior} e o menor é {menor}.')
idade_homem = 0
nome_homem = ''
mulheres = 0
cont = 0
for i in range (1, 5):
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

'''from random import randint
while True:
    jogador =  int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? '))
        print(f'Você jogou {jogador} e o comutador {computador}. total de {total}')'''

    #elif #em loop é secundario



















