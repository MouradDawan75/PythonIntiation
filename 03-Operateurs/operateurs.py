print(">>>>> Opérateurs arithmétiques:")

print("** Addition:")

a = 7
b = 3
c = a + b
c += 2 # équivalent de: c = c + 2
print(f'c = {c}')

print("** Soustraction:")

a = 7
b = 3
c = a - b
c -= 2 # équivalent de: c = c - 2
print(f'c = {c}')

print("** Multiplication:")

a = 7
b = 3
c = a * b
c *= 2 # équivalent de: c = c * 2
print(f'c = {c}')

print("** Division:")

a = 7
b = 3
c = a / b
c /= 2 # équivalent de: c = c / 2
print(f'c = {c}')

print("** Division entière:")

a = 7
b = 3
c = a // b
c //= 2 # équivalent de: c = c // 2
print(f'c = {c}')

print("** Reste de la division entière: modulo")

a = 7
b = 3
c = a % b
c %= 2 # équivalent de: c = c % 2
print(f'c = {c}')

print("** Puissance:")

a = 7
b = 3
c = a ** b
c **= 2 # équivalent de: c = c ** 2
print(f'c = {c}')

print(">>>>> Opérateurs de comparaison:")

# > >= < <= == (égalité), != (différent): renvoient un boolean
nb1 = 7
nb2 = 5

print(nb1 > nb2)
print(nb1 >= nb2)
print(nb1 <= nb2)
print(nb1 < nb2)
print(nb1 == nb2)
print(nb1 != nb2)

print(">>>>> Opérateurs logiques:")
# and, or et not: renvoient un boolean
# Table logique:
# A     B    A and B    A or B
# v     v       v         v
# v     f       f         v
# f     f       f         f      

nb1 = 7
nb2 = 5

print((nb1 > nb2 ) and (nb1 > 0)) # True
print(not(nb1 > nb2)) # False

print(">>>>> Opérateurs: is et in")

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 == list2) # True: car le mm contenu
print(list1 is list2) # False: car 2 objets différents en mémoire

# in permet de vérifier si un élement fait partie pas ou pas d'une collection

print(1 in list1)
print(5 in list2)

prenom = 'Jean' # une chaine est une collection de caractères

print('a' in prenom) # True
print('ea' in prenom) # True
print('Ja' in prenom) # False
print('Ea' in prenom) # False:  Python est case sensitive: sensible à a casse

print('>>>>> Affectations multiples:')

# si des variables sont du mm type et possèdent la mm valeur, on peut faire:

v1=v2=v3=10
print(v1)
print(v2)
print(v3)

# si des variables ne sont pas du mm type, on peut faire: déconseillée en pratique

var1,var2,var3 = 10,True,'test'

# Pour faire des calculs complèxes on peut utiliser le module

import math,statistics

r = math.sqrt(16) # racine carrée
print(r)
math.pow(2,3) # puissance
math.exp(5)
math.factorial(4)

statistics.mean(list1) # moyenne d'une liste