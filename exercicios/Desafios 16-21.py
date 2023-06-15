import math
from math import sin, cos, tan
import random

#Desafio 16
#Num = float(input('digite um número '))
#print(f'o seu número inteiro é {math.floor(Num)}')

#Desafio 17
#Co = float(input('informe o cateto oposto '))
#Ca = float(input('informe o cateto adjacente '))
#H = math.hypot(Co, Ca)
#print(f'A hipotenusa é {H:.2f}')

#Desafio 18
#An = float(input('informe o ângulo '))
#S = sin(math.radians(An))
#C = cos(math.radians(An))
#T = tan(math.radians(An))
#print(f' Seno é {S:.2f}\n Cosseno é {C:.2f}\n Tangente é {T:.2f}')

#Desafio 19
#A1 = input('escreve o nome do primeiro aluno ')
#A2 = input('escreve o nome do segundo aluno ')
#A3 = input('escreve o nome do terceito aluno ')
#A4 = input('escreve o nome do quarto aluno ')
#print(random.choices([A1, A2, A3, A4]))

#Desafio 20
A1 = input('primeiro aluno ')
A2 = input('segundo aluno ')
A3 = input('tercerio aluno ')
A4 = input('quarto aluno ')
S = [A1, A2, A3, A4]
random.shuffle(S)
print(f'A lista é {S}')
