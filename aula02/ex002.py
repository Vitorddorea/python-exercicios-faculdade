'''Crie uma variável nota. Use um desvio condicional para imprimir "Aprovado" se a nota for maior ou igual a 7, "Recuperação" se for entre 5 e 6.9, e "Reprovado" se for menor que 5.'''

nota = float(input('Digite sua nota: '))

if 0 <= nota < 5:
    print('Aluno Reprovado!')
elif 5 <= nota < 7:
    print('Aluno de Recuperação!')
elif 7 <= nota <= 10 :
    print('Aluno Aprovado!')
else:
    print('Nota Inválida!')