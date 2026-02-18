"""Calculadora Simples:
Crie um programa de calculadora. Repita a solicitação de dois números e uma operação. Verifique qual operação foi solicitada e realize o cálculo. Repita esse processo até o usuário digitar "sair"."""

def menu():
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplição')
    print('4 - Divisão')
    print('Digite "sair" para sair')


def somar(n1= 0, n2= 0):
    return n1 + n2

def subtrair(n1=0, n2= 0):
    return n1 - n2

def multiplicar(n1= 0, n2= 0):
    return n1 * n2

def dividir(n1= 0, n2= 0):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return 'Divisao por Zero'
    
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um número válido!')
        
while True:

    print('CALCURADORA')
    menu()

    operacao = input((f'Operação: ')).lower()
    
    if operacao == 'sair': 
        print('Encerrando calculadora ...')
        break
    
    if operacao not in ('1', '2', '3', '4'):
        print('Digite uma opção válida!')
        continue

    n1 = ler_numero('Primeiro número: ')
    n2 = ler_numero('Segundo número: ')
    
    if operacao == '1':
        print(somar(n1, n2))
    elif operacao == '2':
        print(subtrair(n1, n2))
    elif operacao == '3':
        print(multiplicar(n1, n2))
    elif operacao == '4':
        print(dividir(n1, n2))
    


