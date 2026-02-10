'''Crie uma variável dia_da_semana. Use um desvio condicional para imprimir "É dia de semana" se o dia for de segunda a sexta, e "É final de semana" caso contrário.'''

dia_da_semana = int(input('Que dia é hoje? [Seg(1), Ter(2), Qua(3), Qui(4), Sex(5), Sáb(6), Dom(7)]'))


if dia_da_semana in (6,7):
    print('Final de semana')
elif 1 <= dia_da_semana <= 5:
    print('É dia de semana')
else:
    print('Dia inválido')