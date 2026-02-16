'''Soma Total de uma Sequência:
Crie uma variável soma_total com valor inicial 0. Repita a operação de somar cada número de 1 a 50 a soma_total. Ao final, imprima o resultado
'''

soma_total = 0 # acumulador

for c in range(1, 51):
    soma_total += c # soma o valor de atual de c com a soma_total

print(f'Somando os números de 1 a 50 temos o total de {soma_total}')