#DICIONARIOS
pessoas = {'nome': 'Erik', 'idade': 20, 'sexo': 'M'}
'''print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')'''
'''print(pessoas.keys())'''#MOSTRARÁ APENAS A VARIAL NOME IDADE SEXO
'''print(pessoas.values())'''#MOSTRARÁ APENAS ERIK 20 M
'''print(pessoas.items())'''#MOSTRARA AMBOS
'''del pessoas['Sexo']''' #APAGARA A VARIAVEL SEXO
'''pessoas['peso'] = 75''' #COLOCARA MAIS UMA VARIAVEL
'''for k in pessoas.keys(): 
    print(k)'''
'''for k, v in pessoas.items(): #MOSTRA AMBOS EM CADA LINHA
    print(f'{k} = {v}')'''
#DICIONARIO DENTRO DE LISTAS
'''brasil = []
estado1 = {'uf': 'Pernambuco', 'sigla': 'PE'}
estado2 = {'uf': 'Bahia', 'sigla': 'BA'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])'''

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Digite um estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()