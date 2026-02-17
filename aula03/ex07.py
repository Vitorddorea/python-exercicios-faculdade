'''Validação de Senha com Tentativas:
Crie uma senha correta. Repita a solicitação de uma senha ao usuário por 3 vezes. Se ele acertar a senha em alguma das tentativas, imprima "Acesso Concedido" e pare a execução. Se ele errar todas as 3, imprima "Acesso Bloqueado".
'''

senha_correta = 1234

tentativa = 0

while tentativa < 3:
    try:
        senha = int(input('Digite a senha (apenas números): '))
    except ValueError:
        print('\033[31m Digite apenas números! \033[m')
        continue

    tentativa += 1

    if senha_correta == senha:
        print('Acesso Concedido')
        break
    else:
        print(f'Senha Incorreta! Tentativas restantes: {3 - tentativa}')
            
if tentativa == 3:
    print('Acesso Bloqueado')

        
    