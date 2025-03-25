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

print('>>>>>>> Fonctions avec des paramètres optionnels:')

def func(x, alpha=10,beta=15):
    print(x,alpha,beta)

func(99) # utilise les valeurs initales de alpha et beta
func(150,12,32) # en cas de besoin, on peut modifier les valeurs de alpha et beta

# Les paramètres optionnels, possèdent une valeur initiales et sont définis après les paramètres
# obligatoires

# En python, on peut appeler une fonction avec des paramètres nommés sans tenir compte de leur position
# dans la fonction

func(beta=66, x=130)
print(100, end=' ')
print('chaine2')

def prix_ttc(prix_ht:float, tva:float=0.2):
    return prix_ht * (1+tva)

print(prix_ttc(80))
print(prix_ttc(80, tva=0.35)) # si tva change: pas besoin de modifier la fonction

print(">>>>>>>>>>>>> Fonctions qui renvoient plusieurs résultats:")

def somme_et_produit(x,y):
    somme = x + y
    produit = x * y
    return somme,produit

r = somme_et_produit(5,10)
print(type(r))
print(r)
# r est un tuple: c'est une liste non modifiable
# Unpacking: deballage d'un tuple

s,p = r # extraire les élément du tuple r -> s contient le premier élément et p le 2ème
print(s)
print(p)
    

print(">>>>> Fonctions avec un nombre variable de paramètres:")

print(10,True,'test',10.55)

def somme_variable(*entiers:int):
    #print(type(entiers)) -> Python utilise un tuple pour stocker les différents paramètres
    print(entiers)

somme_variable(2,5,8)

print(">>>>> Fonctions natives de Python:")

lst = [2,5,10]

print(sum(lst))
print(min(lst))
print(max(lst))
print(len(lst)) # renvoie le nombre d'éléments
print(round(3.5689,2))

import statistics

print(statistics.mean(lst)) # la moyenne

#quit() : mettre fin à l'exécution du script en cours

print('>>>>>>>>>>> Variables locales - Variables globales:')

# b et c sont visibles dans tout le script: varibales globales
b = 10
c = 10

def modifier():
    # les variables définies dans une fonctions, sont visibles
    # uniquement dans la fonction, appelées variables locales
    global b # on demande à la fonction de manipuer le b global
    b = 15
    c = 15
    v = 50
    print("************************************")
    print(locals())
    print("************************************")

modifier()

print(f'b = {b}')
print(f'c = {c}')

print(globals())

chemin = "c:\\test.txt"


def lecture():
    global chemin

def ecriture():
    global chemin



