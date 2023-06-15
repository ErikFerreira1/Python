peso = input('qual é seu peso?')
altura = input('qual a sua altura?')
altura2 = float(altura) * float(altura)
imc = float(peso) / float(altura2)
print('seu imc é {}'.format(imc))
if imc <18.5:
 print('seu imc é {}'.format(imc))
 print('imc acusou magreza')
elif imc >= 18.5 and imc < 24.9:
 print('seu imc é {}'.format(imc))
 print('imc acusou normal')
elif imc >= 25 and imc < 29.9:
 print('seu imc é {}'.format(imc))
 print('imc acusou sobrepeso')
elif imc >= 30 and imc < 39.9:
 print('seu imc é {}'.format(imc))
 print('imc acusou obesidade')
elif imc > 40:
 print('seu imc é {}'.format(imc))
 print('imc acusou obesidade grave')

