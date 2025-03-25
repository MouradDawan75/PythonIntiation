age = 50
prenom = 'Marie'

# Concaténation: conversion des types numériques en str obligatoire
print('Prénom: '+prenom+' Age: '+str(age))

# Utiliser une virgule comme séparateur: la virgule génère un espace
# Aucune conversion en str nécessaire
print('Prénom:',prenom,'Age:',age)

# A partir de Python 3: ajout de la fonction format()

print('Prénom: {} age: {}'.format(prenom,age)) # tenir compte de l'ordre des accolades

# A partir de Python 3.6: ajout de fstring -> syntaxe simplifiée de la fonction format

print(f'Prénom: {prenom} Age: {age}')

# Entre accolades, on peut soit insérer des varaibles, soit des expressions

print(f'{3 + 5}') # exemple d'une expression

print('>>>>>>>> Chaine multilignes:')

# chaine verbatime

print("""
    Ceci est 
une chaine
sur plusieurs lignes.
""")

print('''
    Ceci est 
une chaine
sur plusieurs lignes.
''')

# Les caractères d'échappement
# \r et \n: retour à la ligne
# \s: space
# \b: backspace
# \t: tabulation

print('\tCeci est\nune chaine\nsur plusieurs lignes.')

chemin = 'c:\\test\\notes.xml'

print("ceci est du \"texte\"")
print('ceci est du "texte"')


print('chaine1',end=" ") # chaine1\n
print('chaine2') # chaine2\n

print('s1','s2',sep=':')