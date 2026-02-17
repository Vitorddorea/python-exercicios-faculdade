'''Tabuada:
Peça ao usuário para digitar um número de 1 a 10. Repita a multiplicação desse número de 1 a 10 e imprima o resultado de cada linha da tabuada.'''

print('=-' * 10)
print('TABUADA'.center(20))
print('=-' * 10)

while True:
    try:
        num = int(input('Digite um número de 1 a 10: '))
        if  1 <= num <=10:
            break
        else:
            print('\033[31m Número inválido! \033[m' )
            continue
    except ValueError:
        print('\033[31m Digite um número inteiro! \033[m')
        continue

print('=-' * 10)
print(f'Tabuada do {num}'.center(20))
print('=-' * 10)

for i in range(1, 11):
    print(f'{i} x {num} = {i * num}')
        