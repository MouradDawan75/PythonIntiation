# list: est une collection ordonnée avec doublons autorisés

# liste vide: 2 syntaxes

l1 = []
l2 = list()

print(l1)
print(l2)

# Aucune restriction sur le type d'éléments d'une liste en Python.

lst = [10,25.5,True,'test', [15,12]]

notes = [2,6,7,9]
print(notes)

# Ajouts:

notes.append(6)
print(notes)

notes.insert(0,9)
print(notes)

print(notes.count(6))
print(notes.index(6)) # index commence à 0

# Modifications:

notes[0] = 99
print(notes)

# Suppressions:

notes.remove(6)
print(notes)

print(notes.pop()) # supprime et renvoie le dernier élément par défaut

notes.extend([10,11])
print(notes)

print(">>>>> Atteindre un élément:")

notes = [2,6,7,9]

taille = len(notes)

print(f'Première note: {notes[0]}')
print(f'Dernière note: {notes[taille - 1]}')

# Python autorise les indexs négatifs:
print(f'Dernière note: {notes[-1]}')

print(">>>>>>>>> Parcourir une liste:")

notes = [2,6,7,9]

print('>>FOR:')

for n in notes:
    print(n)

print('>>WHILE:')

taille = len(notes)
compteur = 0

while compteur < taille:
    print(notes[compteur])
    compteur += 1

print(">>>> Slicing:")
# Slincing: mécaninsme permettant de créer des sous listes à partir de istes existantes

prenoms = ['Vincent','Thomas','Louis','Luc']

list1 = prenoms[0:3] # de index 0 à 2 (n - 1)
print(list1)

list2 = prenoms[:3] # du début jusqu'à 2 (n - 1)
print(list2)

list3 = prenoms[:] # du début jusqu'à la fin -> une copie
print(list3)

list4 = prenoms[::2] # du début jusqu'à la fin avec un pas de 2
print(list4)

print('>>> affichez les 3 premiers éléments:')
print(prenoms[:3])

print('>>> affichez les 3 derniers éléments:')
print(prenoms[-3:])

print(">>>>> Comprehension List:")
#Liste en compréhension: mécanisme permettant de créer de nouvelles liste à partir 
# de listes existantes en modifiant le contenu des listes de départ

nombres = range(10) 

# nouvelle liste en doublant (multiplier par 2) tous les éléments
# syntaxe classique:
nombres_doubles = []

for e in nombres:
    nombres_doubles.append(e * 2)

# Comprehension List: syntaxe simplifiée

nombres_doubles_new = [e * 2 for e in nombres]

nombres = range(10)

# Nouvelle liste ne contenant que les nombres impaires

nombres_impairs = [e for e in nombres if e % 2 != 0]

# syntaxe classique:

nombres_impairs_classique = []

for e in nombres:
    if e % 2 != 0:
        nombres_impairs_classique.append(e)

print(nombres_impairs)
print(nombres_impairs_classique)

nombres =  range(10)

# Nouvelle liste en inversant uniquement les nombres impaires: 0,-1,2,-3,4.....

# syntaxe classique:
nombres_inverses_classique = []

for e in nombres:
    if e % 2 != 0:
        nombres_inverses_classique.append(-e)
    else:
        nombres_inverses_classique.append(e)

print(nombres_inverses_classique)

# Comprehension list:

nombres_inverses = [e if e % 2 == 0 else -e for e in nombres]

lst = [10,2,1,15,2,7,1,6,5]

# Affichez le nombre d'élément supérieurs à 2

# Comprehension List:

print(len([e for e in lst if e > 2]))

# Syntaxe classique:

compteur = 0
for e in lst:
    if e > 2:
        compteur += 1


print(compteur)