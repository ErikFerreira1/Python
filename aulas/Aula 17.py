#LISTAS
num = [2, 3, 4, 9]
num[2] = 5
num.append(7)#ADICIONA MAIS VALORES A LISTA
num.sort(reverse=True)#ORDEM CRESCENTE #REVERSE=TRUE ORDEM DECRESCENTE
num.insert(2, 2)#IRÁ COLOCAR NA POSIÇÃO 2 O NÚMERO 0
'''num.pop(2)'''#REMOVERÁ ELEMENTOS NA POSIÇÃO DETERMINADA
'''num.remove(7)'''#REMOVERÁ ESPECIFICAMENTE O VALOR DESEJADO
if 5 in num: #PARA REMOVER NÚMEROS QUE AINDA NÃO ESTÃO NA LISTA
    num.remove(5)
else:
    print('Não tem número 4')
print(num)
print(f'ESSA LISTA TEM {len(num)} ELEMENTOS')

valores = []
for cont in range(0, 5):
    valores.append((int(input('Digite um valor: '))))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a[:] #B RECEBERÁ UMA COPIA DE A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')