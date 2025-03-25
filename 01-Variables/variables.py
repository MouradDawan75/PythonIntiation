# Variable: zone mémoire contenant une valeur typée

# Types de données de python:

# types numériques: int (entiers), float (réels), complex
# type textuel: str (string)
# type boolean: True/False
###### COllections:
# listes: range, tuple(), list []
# ensemble: set
# dictionnaire: dict

# Python utilise le typage dynamique. Pas besoin de spécifier le type d'une variable
# En Java, le typage est statique: int x = 10


entier = 10

# 2 syntaxes pour le type textuel
chaine1 = 'ceci est une chaine'
chaine2 = "autre chaine"
my_bool = True
flottant = 10.5
complexe = 4 + 2j # j est le nombre imaginaire

print(entier)
print(chaine1)
print(chaine2)
print(complexe.real)
print(complexe.imag)

# Règles de nommage:
# 1) Le nom d'une variabe peut contenir, des lettres, des chiffres et underscore et ne peut
# pas commencé par un chiffre
# 2) Python utilise la convention snake_case pour les noms composés
# PascalCase: MaVariable
# camelCase: maVariable
# snake_case: ma_variable -> convention utilisée par Python

# Constante: est une variable dont le contenu ne peut pas étre modifié

# La notion de constante, n'exuste pas réellement en Python, 
# c'est juste une convention de nommage

MA_CONSTANTE = 50
MA_CONSTANTE = 'texte'

print(MA_CONSTANTE)

# Variable nulle: None
x = None

print(x)

print(">>>>>>>>>> l'id des variables")

x = 10
print(id(x))

y = x
print(id(y))

print(">>>>>>> Type des variables: ")

i = 10
print(type(i))

s = 'texte'
print(type(s))

f = 10.5
print(type(f))

# On a une certaine liberté dans l'écriture des flottants:
n = 0.99
n = 00.99
n = .99

# Pour les grands nombres: pour les rendre plus lisibles, on peut faire:

nb = 589_258_456 
print(type(nb))
print(nb)

print(">>>>> Conversions de types:")

x = 10.5
i = int(x)

x = float(i)

s = '55'
v = int(s)

nb1 = int(input('Premier nombre: '))
nb2 = int(input('Second nombre: '))

somme = nb1 + nb2

print("Résultat = "+str(somme)) # En Python, on ne peut concaténer que des chaines

import random

a = random.randint(1,10)

print(a)

