'''Soma de Pares e Ímpares:
Crie duas variáveis para a soma de pares e ímpares. Repita a verificação de cada número de 1 a 100. Se o número for par, some-o à variável de pares; se for ímpar, some-o à variável de ímpares. Exiba o total de cada somatória no final.'''

soma_pares =  soma_impares = 0

for c in range(1,101):
    if c % 2 == 0:
        soma_pares += c
    else:
        soma_impares += c

print(f'Somando os números pares de 1 a 100 temos {soma_pares}')
print(f'Somando os números ímpares de 1 a 100 temos {soma_impares}')