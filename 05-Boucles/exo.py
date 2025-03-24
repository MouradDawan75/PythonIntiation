# 1) Affichez tous les nombres de 1 (inclus) à 10 (inclus) -> fct range

print(">>>>>>>>> exo1:")
#sol1:
for e in range(10):
    print(e+1)


#sol2:
for e in range(11):
    if e != 0:
        print(e)

#sol3: on peut modifier l'élément de départ à 0 par défaut
for e in range(1,11):
    print(e)

# 2) Affichez uniquement les nombres pairs  de 1 (inclus) à 10 (inclus) -> fct range

print(">>>>>>>>> exo2:")

# sol1:
for e in range(1,11):
    if e % 2 == 0:
        print(e)

# sol2: on peut aussi modifier le pas qui s'incrémente de 1 par défaut

for e in range(2,11,2):
    print(e)


print(">>>>>>>>> exo3:")
#3)

compteur = 0

while True:
    choix = input("""

    1- Addition: tapez a
    2- Soustraction: tapez s
    3- Multiplication: tapez m
    4- Division: tapez d
    5- Quitter: tapez q

    choisir une opération: 
  
  """)
    
    # Gestion du break
    if choix == 'q':
        print('Fin du programme')
        break

    # Gestion d'un choix non valide
    # if choix != 'a' or choix != 's' or choix != 'm' or choix != 'd':
    #     print('choix invalide.....')
    #     continue

    if choix not  in 'asmd': # if choix not in ['a','s','m','d']:
        print('choix invalide.....')
        compteur += 1
        if compteur == '3':
            print('Pas plus de 3 tentatives.')
            break 
        continue

    # Demandez la saisie de 2 nombres

    nb1 = float(input('Premier nombre: '))
    nb2 = float(input('Second nombre: '))
    compteur = 0

    # Gestion de la division par 0
    if choix == 'd' and nb2 == 0:
        #demandez un second nombre différent de 0
        while True:
            nb2 = float(input('Second nombre différent de 0 : '))
            if nb2 != 0:
                break

    # Affichez le résultat:

    match choix:

        case 'a':
            print(f'{nb1} + {nb2} = {nb1 + nb2}')

        case 's':
            print(f'{nb1} - {nb2} = {nb1 - nb2}')

        case 'm':
            print(f'{nb1} x {nb2} = {nb1 * nb2}')

        case 'd':
            print(f'{nb1} / {nb2} = {nb1 / nb2}')


print(">>>>>>>>>>>> Solution avec une boucle finie:")
        
choice = 'x'

while choice != 'q':

    choice = input("""

    1- Addition: tapez a
    2- Soustraction: tapez s
    3- Multiplication: tapez m
    4- Division: tapez d
    5- Quitter: tapez q

    choisir une opération: 
  
  """)
    
    if choice == 'q':
        print('Fin...............')
        continue 
    
    
    # Gestion d'un choix non valide
    # if choix != 'a' or choix != 's' or choix != 'm' or choix != 'd':
    #     print('choix invalide.....')
    #     continue

    if choice not  in 'asmd' : # if choix not in ['a','s','m','d']:
        print('choix invalide.....')
        continue

    # Demandez la saisie de 2 nombres

    nb1 = float(input('Premier nombre: '))
    nb2 = float(input('Second nombre: '))

    # Gestion de la division par 0
    if choix == 'd' and nb2 == 0:
        #demandez un second nombre différent de 0
        while True:
            nb2 = float(input('Second nombre différent de 0 : '))
            if nb2 != 0:
                break

    # Affichez le résultat:

    match choice:

        case 'a':
            print(f'{nb1} + {nb2} = {nb1 + nb2}')

        case 's':
            print(f'{nb1} - {nb2} = {nb1 - nb2}')

        case 'm':
            print(f'{nb1} x {nb2} = {nb1 * nb2}')

        case 'd':
            print(f'{nb1} / {nb2} = {nb1 / nb2}')