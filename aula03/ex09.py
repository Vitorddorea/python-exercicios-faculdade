"""Detector de Vogais e Consoantes:
Peça ao usuário uma palavra. Repita a verificação de cada letra da palavra. Se a letra for uma vogal, conte-a como vogal; se for uma consoante, conte-a como consoante. Ao final, imprima o total de cada um."""

vogal = 0
consoante = 0 

palavra = input('Digite uma palavra: ').lower()

for letra in palavra:
    if letra in 'aeiou':
        vogal += 1
    elif letra.isalpha():
        consoante += 1

print(f'A palavra {palavra} tem {vogal} vogais e {consoante} consoante')
