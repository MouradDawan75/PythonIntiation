# 1) Demandez la saisie d'un nombre. Affichez si le nombre saisi est pair ou impair
nb = int(input('Votre nombre: '))

if nb % 2 == 0:
    print(f'{nb} est pair')
else:
    print(f'{nb} est impair')

# 2) Demandez la saisie d'un mot. Affichez si le mot saisi contient ou pas la lettre e

mot = input('Votre mot: ')

if 'e' in mot or 'E' in mot:
    print(f'{mot} contient e')
else:
    print(f'{mot} ne contient pas e')