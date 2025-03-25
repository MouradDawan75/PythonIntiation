# set: est une collection non ordonnée sans doublons. De plus, le type set supportes
# les opérations sur les ensembles, telles que l'union, l'intersection, la différence et
# la différence symétrique

# set vide:

s = set()

panier = {'pomme','orange','banane','orange'}

print(panier)

a = set('abracadabra') # conversion d'une chaine en set
b = set('alacazam')

print(a)
print(b)

print(">>>> Union:")
# lettres dans a ou dans b ou dans les 2
# 2 syntaxes:
print(a | b)
print(a.union(b))

print('>>> Intersection:')
# lettres dans a et dans b
# 2 syntaxes:
print(a & b)
print(a.intersection(b))

print(">>>> Différence:")
# lettres dans a mais pas dans b
# 2 syntaxes:
print(a - b)
print(a.difference(b))

print(">>> Différence symétrique:")
# lettres dans a ou dans b mais pas dans les 2
# 2 syntaxes:
print(a ^ b)
print(a.symmetric_difference(b))

#ajouts
a.add('b')

# suppressions:
a.remove('a')
a.pop()

# Suppression des doubons dans une liste
lst = [1,1,2,2,3,3]

# conversion en set:
lst = set(lst)
lst = list(lst)

print(lst)
