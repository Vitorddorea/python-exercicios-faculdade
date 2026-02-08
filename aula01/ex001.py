'''Crie uma variável nome com seu nome, uma variável idade com sua idade e uma variável altura com sua altura. Imprima uma frase que use todas as variáveis.'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

print(f'O seu nome é {nome}, sua idade é {idade} e você tem {altura:.2f}m de altura.')