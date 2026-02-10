'''Crie uma variável numero_inteiro e verifique se ele é par ou ímpar usando o operador resto divisão (o %). Imprima a resposta.'''

numero_inteiro = int(input('Digite um número inteiro: '))

if numero_inteiro % 2 == 0:
    print(f'O número {numero_inteiro} é Par')
else:
    print(f'O número {numero_inteiro} é Ímpar')