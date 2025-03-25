# tuple: est une collection ordonnée avec doublons autorisés.
# Un tuple est une liste en lecture seule (non modifiable)

# tuple vide: 2 syntaxes:
t1 = ()
t2 = tuple()

prenoms = ('Thomas', 'Luc', 'Louis')

prenoms.count('Thomas')
prenoms.index('Luc')

#prenoms[0] = 'Dawan'

# Unpacking: deballage d'un tuple

p1,p2,p3 = prenoms
print(p1)
print(p2)
print(p3)

# Modification d'un tuple:
# 1- conversion en liste

prenoms = list(prenoms)

#2- appliquer les modifications

prenoms.remove('Thomas')
prenoms.append('Dawan')

# 3- conversion en tuple
prenoms = tuple(prenoms)

print(prenoms)