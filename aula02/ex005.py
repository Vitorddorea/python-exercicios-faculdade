'''Crie uma variável velocidade e uma variável limite_velocidade. Use um desvio condicional para imprimir "Velocidade OK", "Multado" ou "Perigo, velocidade muito alta" dependendo da situação.'''

limite_velocidade = 45

sua_velocidade = int(input('Qual sua velocidade atual? '))

if sua_velocidade <= limite_velocidade:
    print('Velocidade OK')
else: 
    print('Multado, velocidade acima do permitido.')