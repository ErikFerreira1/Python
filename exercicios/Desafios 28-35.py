#Desafio 28
import random
'''Numero = random.randint(0,5)
A = int(input('Tente descobrir o número que o computador pensou entre 0 e 5: '))
if A == Numero:
    print('Você acertou o número!\nPARABÉNS!')
else:
    print('Você Errou o número! \nTente novamente!')
print(f'O número era: {Numero}')'''

#Desafio 29
'''Velocidade = int(input('Escreva a velocidade do carro: '))
Multa = (Velocidade - 80) * 7
if Velocidade >80:
    print(f' Você foi mutado!\n Valor da multa foi R${Multa}')
else:
    print('Você não foi multado!')'''

#Desafio 30
'''PI = int(input('digite o numero: '))
Cal = PI / 2
if Cal.is_integer() == True:
    print("É Par")
else:
    print("É impar")'''

#Desafio 31
'''Distancia = int(input('Qual a distância da viagem? '))
if Distancia <= 200:
    Cal = Distancia * 0.5
    print(f'A viagem foi de {Distancia}Km, o preço da passagem é R${Cal}')
else:
    Cal2 = Distancia * 0.45
    print(f'A viagem foi de {Distancia}Km, o preço da passagem é R${Cal2}')'''

#Desafio 32
'''Ano = int(input('Digite algum ano: '))
Cal = Ano % 4
if Cal == 0:
    print(f'O ano {Ano} é bissexto')
else:
    print(f'O ano {Ano} não é bissexto')'''

#Desafio 33
'''N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))
N3 = int(input('Digite o terceiro número: '))
if N1 > N2 and N1 > N3:
    print(f'{N1} é o maior')
if N2 > N1 and N2 > N3:
    print(f'{N2} é o maior')
if N3 > N2 and N3 > N1:
    print(f'{N3} é o maior')

if N1 < N2 and N1 < N3:
    print(f'{N1} é o menor')
if N2 < N1 and N2 < N3:
    print(f'{N2} é o menor')
if N3 < N2 and N3 < N1:
    print(f'{N3} é o menor')'''

#Desafio 34
'''Salario = float(input('Informe o seu salario: R$'))
Tabela = str(input(' Salários a cima de R$1250 o aumento é de 10%.\n Salários a baixo de R$1250 o Aumento é de 15%.'))
if Salario > 1250:
    A = (Salario * 10 / 100) + Salario
    print(f'Seu salário com aumento ficou: R${A} ')
if Salario < 1250:
    B = (Salario * 15 /100) + Salario
    print(f'Seu salário com aumento ficou: R${B}')'''

#Desafio 35

L1 = float(input('Digite o primeiro lado do triangulo: '))
L2 = float(input('Digite o segundo lado do triangulo: '))
L3 = float(input('Digite o terceiro lado do triangulo: '))
if L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1:
    print('É possivel formar um triângulo!')
else:
    print('Não é possível formar o triângulo!')