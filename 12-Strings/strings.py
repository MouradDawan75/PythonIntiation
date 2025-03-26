chaine = 'test'
chaine = chaine.upper()

# le type string est immuable

print(chaine)

texte = ' ceci est une chaine '

print(texte.strip()) # suppression des espaces en début et fin de chaine
print(texte.rstrip()) # suppression des espaces en début et fin de chaine
print(texte.startswith('ceci'))
print(texte.endswith('chaine '))
print(len(texte))
print(texte.replace('e', 'a'))
print(texte.replace('e', 'a', count=2))

print(texte.split())