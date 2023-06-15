'''def soma(a, b):
    s = a + b
    print(f'A soma entre A e B é {s}')


soma(5, 9)'''

'''def contador(*num):
    print(num)

contador(2, 5, 6, 7, 8)
contador(3, 5)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1
valores = [2, 3, 4, 6, 8]
dobra(valores)
print(valores)