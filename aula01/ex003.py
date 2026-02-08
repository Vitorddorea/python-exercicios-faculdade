'''Crie uma variável peso e uma variável altura. Use um operador para calcular o IMC (Índice de Massa Corporal) e imprima o resultado.'''

from time import sleep

print('-=' * 15)
print('Calculo de IMC'.center(30))
print('-=' * 15)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# IMC = peso / altura ao quadradro
imc = peso / altura ** 2

print('Calculando...')
sleep(0.5)

print(f'Seu IMC é {imc:.1f}')

# EXTRA: Conferindo a situação do IMC  

# Classificação do IMC segundo a OMS
if imc < 18.5:
    print('Abaixo do peso')
elif  18.5 <= imc < 24.5:
    print('Peso normal')
elif 25 <= imc < 34.99:
    print('Acima do peso')
else:
    print('Obesidade')

    