'''Crie uma variável idade. Use um desvio condicional para imprimir "Maior de idade" se a idade for 18 ou mais, e "Menor de idade" caso contrário.'''

#Biblioteca para informar o tempo
from datetime import date 

nasc = int(input('Digite seu ano de nascimento: '))

#Define sua idade subtraindo seu ano de nascimento pelo ano atual
idade = date.today().year - nasc 

print(f'Você tem {idade} anos de idade.')

if idade >= 18: 
    print('Maior de idade')
else:
    print('Menor de idade')