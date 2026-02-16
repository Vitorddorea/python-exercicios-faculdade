'''Crie uma variável senha_correta = "python123" e uma variável senha_digitada. Verifique se a senha digitada está correta e imprima uma mensagem de sucesso ou erro.'''

senha_correta = 'python123'

senha_digitada = input('Qual a senha? ')

if senha_correta == senha_digitada:
    print('Senha correta!')
else: 
    print('Senha incorreta!')