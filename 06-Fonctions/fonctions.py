# Fonction: est un ensemble d'instructions réutilisable
# Fonction qui renvoie un résultat: ex: input()
# Fonction qui ne revoie aucun aucun résultat: ex: print()

# Syntaxe: def nom_fonction(paramètres): instrcutions

# Exemple d'un fonction

def my_fonction():
    print('test my fonction......')

# Appelle de my_fonction:
my_fonction()

# Sans les parenthèses, il s'agit d'une variable contenant l'id de la fonction
my_fonction

f = my_fonction
f()

# Exemple d'une fonction avec des paramètres:

# pour commenter des lignes sélectionnées: ctr + k + ctr + c
# pour décommenter des lignes sélectionnées: ctr + k + ctr + u

def repeter(message, nombre_de_fois):
    # for i in range(nombre_de_fois):
    #     print(message)

    compteur = 0
    while compteur < nombre_de_fois:
        print(message)
        compteur += 1

repeter('hello', 5)


# Exemple d'une fonction qui renvoie un résultat

def carre(x):
    return x ** 2

r = carre(5)
print(r)

def somme(x,y):
    return x+y

print(somme(10, 5))

#print(somme('test',5))

# Annotations de types: moyen permettant aux développeurs de spécifier le
# type de paramètres attendus par une fonction

x:int = 10
s:str = 'test'

def add(x:int, y:int) -> int:
    return x+y

# Le typage reste dynamique tout le temps, même en pratiquant les annotations de types.