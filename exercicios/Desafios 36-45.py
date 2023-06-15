#Desafio 36
'''Valor_Casa = float(input('Informe o valor da casa R$'))
Salario = float(input('Informe o seu salário R$'))
Anos = int(input('Informe quantos anos vai pagar a casa: '))
M = Anos * 12
P = Valor_Casa / (Anos * 12)
S = (Salario * 30) / 100
if P > S:
    print('\033[31mEmprestimo negado!')
else:
    print(f'\033[32m Emprestimo aprovado!\n \033[mTotal de meses a pagar: {M} Meses \n Valor da parcela mensal é: R${P:.2f}')'''

#Desafio 37
'''Num = int(input('Insira um número para convesão: '))
Base = int(input('Qual será a base?\n[1] \033[97mbinario\n[2] \033[97moctal\n[3] \033[97mhexadecimal\nDigite qual será a base: '))
if Base == 1:
    A = bin(Base)
    print(f'{Num} Convertido para binario é \033[32m{A}')
elif Base == 2:
    B = oct(Base)
    print(f'{Num} Convertido para octadecimal é \033[32m{B}')
elif Base > 3:
    print('\033[31mNúmero invalido')
else:
    C = hex(Num)
    print(f'{Num} Convertido para hexadecimal é \033[32m{C}')'''

#Desafio 38
'''Num = int(input('Digite o primeiro número: '))
Num2 = int(input('Digite o segundo número: '))
if Num > Num2:
    print('O primeiro número é maior')
elif Num < Num2:
    print('O segundo número é maior')
elif Num == Num2:
    print('Os valores são iguais')'''

#Desafio 39
'''Ano = int(input('Digite o ano que você nasceu: '))
Alistamento = 2023 - Ano
AP = 18 - Alistamento
if Alistamento < 18:
    print(f'Você tem {Alistamento} anos, ainda falta {AP} ano(s) para se alistar!')
elif Alistamento > 18:
    print(f'Você tem {Alistamento} anos, já passou {Alistamento - 18} ano(s) do seu alistamento!')
elif Alistamento == 18:
    print(f'Você tem {Alistamento} anos, está na hora de se alistar no exercito!')'''

#Desafio 40
'''Nota1 = float(input('Digite sua primeira nota: '))
Nota2 = float(input('Digite sua segunda nota: '))
Media = (Nota1 + Nota2) / 2
if Media < 5.0:
    print(f'Sua nota foi: {Media} \n\033[31mReprovado!')
elif Media >= 5 and Media < 6.9:
    print(f'Sua nota foi: {Media} \n\033[31mRecuperação!')
elif Media > 7:
    print(f'Sua nota foi {Media} \n\033[32mAprovado!')'''

#Desafio 41
'''idade = int(input('Ano de nascimento: '))
ano = 2023 - idade
if ano <= 9:
    print(f'Sua idade é: {ano}. Sua categoria é: \033[32mMirim')
elif ano <= 14:
    print(f'Sua idade é: {ano}. Sua categoria é: \033[32mInfantil')
elif ano <= 19:
    print(f'Sua idade é: {ano}. Sua categoria é: \033[32mJunior')
elif ano <= 20:
    print(f'Sua idade é: {ano}. Sua categoria é: \033[32mSênior')
elif ano > 20:
    print(f'Sua idade é: {ano}. Sua categoria é: \033[32mMaster')'''

#Desafio 42
'''L1 = float(input('Digite o primeiro lado do triangulo: '))
L2 = float(input('Digite o segundo lado do triangulo: '))
L3 = float(input('Digite o terceiro lado do triangulo: '))
if L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1:
    print('É possivel formar um triângulo!')
    if L1 == L2 == L3:
        print('Todos lados iguais, triangulo equilátero')
    elif L1 == L2 or L2 == L3:
        print('Dois lados iguais, triangulo Isósceles')
    elif L1 != L2 and L2 != L3 and L1 != L3:
        print('Todos lados diferentes, triangulo escaleno')
else:
    print('Não é possível formar o triângulo!')'''

#Desafio 43
'''Peso = float(input('Digite seu peso: '))
Altura = float(input('Digite a sua altura: '))
Imc = Peso / (Altura * Altura)
print(f'Seu imc é {Imc:.2f}')
if Imc < 18.5:
    print('Abaixo do peso')
elif Imc >= 18.5 and Imc < 25:
    print('Peso ideal')
elif Imc >= 25 and Imc < 30:
    print('Sobrepeso')
elif Imc >= 30 and Imc < 40:
    print('Obesidade')
elif Imc > 40:
    print('Obesidade mórbida')'''

#Desafio 44
'''print('\033[31m=-\033[m'*30)
Preco = float(input('\033[97mQual o valor das compras? R$'))
print('\033[31m=-\033[m'*30)
Pagamento = int(input('\033[97mQual será a forma de pagamento?\n[1] À VISTA DINHEIRO\n[2] À VISTA CARTÃO\n[3] CARTÃO 2X\n[4] CARTÃO 3X MAIS\nSelecione uma forma de pagamento:'))
print('\033[31m=-\033[m'*30)
if Pagamento == 1:
    A = Preco - (Preco * 10) / 100
    print(f'\033[97mValor da sua compra: R${Preco}\nÀ vista no dinheiro fica: R${A}')
elif Pagamento == 2:
    B = Preco - (Preco * 5) / 100
    print(f'\033[97mValor da sua compra: R${Preco}\nÀ vista no cartão fica: R${B}')
elif Pagamento == 3:
    print(f'\033[97mValor da sua compra: R${Preco}')
elif Pagamento == 4:
    C = (Preco * 20) / 100 + Preco
    print(f'\033[97mValor da sua compra: R${Preco}\nÀ prazo 3x mais no cartão fica: R${C}')'''
#Desafio 45
import random
'''print('='*20, '\033[36mVAMOS JOGAR JOKENPÔ\033[m', '='*20)
print('\033[97mESCOLHA ENTRE: PEDRA, PAPEL E TESOURA')
ESCOLHA = str(input('QUAL É A SUA ESCOLHA? ')).upper()
print('\033[35mPROCESSANDO...\033[m')
A = 'PEDRA', 'PAPEL', 'TESOURA'
COMPUTADOR = random.choice(A)
print(f'O COMPUTADOR ESCOLHEU \033[33m{COMPUTADOR}')
if ESCOLHA == COMPUTADOR:
    print('\033[97mEmpate')
elif ESCOLHA == 'PEDRA' and COMPUTADOR == 'PAPEL'or ESCOLHA == 'PAPEL' and COMPUTADOR == 'TESOURA' or ESCOLHA == 'TESOURA' and COMPUTADOR == 'PEDRA':
    print('\033[31mO COMPUTADOR VENCEU\033[m')
elif ESCOLHA == 'PAPEL' and COMPUTADOR == 'PEDRA'or ESCOLHA == 'TESOURA' and COMPUTADOR == 'PAPEL' or ESCOLHA == 'PEDRA' and COMPUTADOR == 'TESOURA':
    print('\033[32mPARABÉNS! VOCÊ VENCEU!\033[m')'''














