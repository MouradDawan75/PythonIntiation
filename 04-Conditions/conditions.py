# Bloc conditionnel: est un ensemble d'instructions qui ne s'exécute que si
# une condition est vérifiée

age  = 26

if age < 18 :
    print('mineur')
    print('Toujours mineur')

print('fin du bloc.....')

# les : représente le début du bloc d'instructions. Tant que les instructions 
# sont indentées de la mm façon, on est toujours dans le mm bloc

if age < 18 :
    print('mineur')
elif age <= 25:
    print('jeune adulte')
else:
    print('adulte')

# On peut aussi combiner des conditions en utilisant les opérateurs logiques:

# On peut ajouter des parenthèses en cas de besoin

if (age >= 18) and (age <= 25):
    print('Vous avez entre 18 et 25 ans')

derogation = True

if (age >= 18) or (derogation == True):
    print('Au moins 18 ans ou avoir une dérogation')

# Un bloc vide n'est pas valide syntaxiquement. 
# Pour que e boc vide soit valide syntaxiquement, on peut utiliser le mot clé pass

if age < 18 :
    pass
    # a compléter plus tard


print('suite du script')

# Depuis Python 3.10, ajout du match/case qui permet de remplacer les elif qui s'imbriques

note = 500

match note:

    case 0|1|2|3|4|5|6|7|8|9:
        print('En dessous de la moyenne')

    case 10|11|12|13:
        print('Juste la moyenne')

    # pour les autres cas, 2 syntaxes:
    # soit case other ou case _:
    case other:
        print('Good job')

    # case _:
    #     print('good job')


