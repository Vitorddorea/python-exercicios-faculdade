'''Imprimindo Números e Contando Múltiplos:
Repita a impressão dos números de 1 a 30. No final, exiba a quantidade de números múltiplos de 2 e a quantidade de números múltiplos de 3'''

mult2 = 0
mult3 = 0

print('Contando de 1 a 30: ')

for c in range(1, 31):
    print(c, end=' ')
    # confima se o numero é múltiplo de 2 pelo resto da divisão por 2 ou 3 e adiciona ao contador
    if c % 2 == 0:
        mult2 += 1 

    if c % 3 == 0:
        mult3 += 1    
    
    
print()
print(f'De 1 a 30 tem {mult2} mútiplos de 2 e {mult3} múltiplos de 3')