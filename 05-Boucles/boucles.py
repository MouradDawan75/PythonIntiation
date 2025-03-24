# Boucle for:
# 1- Permet de parcourir tous les élements d'une collection
# 2- Si on connait le nombre d'itérations d'un bloc d'instructions

# Boucle while: boucle conditonnelle
# Permet de gérer un traitement répététif dont le nombre d'itérations n'est pas connu
# mais qui dépend d'un condition.

print(">>>>>>>>>> Boucle for:")

# 1- Parcourir une collection
nombres = range(10) # renvoie une liste d'entiers alant de 0 à 9 (s'arrête à n - 1)

for i in nombres:

    # sortir du for si l'élément en cours est égale 5
    if i == 5:
        break
    print(i)

prenom = 'Jean' # une chaine est une collection de caractères

for lettre in prenom:
    print(lettre)

# 2- bloc répététitif dont le nbre d'itération est connu:
# affichez 5 fois la chaine hello

for i in range(5): # [0,1,2,3,4]
    print('hello')


for i in range(3):
    password = input('Votre mot de passe: ')


print(">>>>>>>>>> Boucle while:")



# Tant que la condtion est vraie: la boucle while s'exécute.
x = 0

while x < 5:
    print(f'Passage {x}')
    x += 1 # x = x + 1



# lire un nombre compris entre 1 et 10.
# Tant que le nombre saisi n'est pas compris entre 1 et 10, redemandez la saisie d'un autre


# Solution avec une bouce infinie:

print ('>>>>>>> while infinie:')
while True:

    nb = int(input('Nombre entre et 10: '))
    if nb >= 1 and nb <= 10:
        break # break permet de sortir de la boucle inifie
        
        



# Solution sans utiliser une boucle infinie:


print ('>>>>>>> while finie:')
nombre  = 0 # la boucle s'exécute au moins 1 fois
while not(nombre >= 1 and nombre <= 10):
    nombre = int(input('Votre nombre entre 1 et 10: '))


# Demandez la saisie d'un  nombre pair.

# boucle infinie:
while True:

    nb = int(input('Votre nombre:'))
    if nb % 2 == 0:
        break
    else: 
        print('nombre invalide....')


# boucle finie:

n = 1
while not(n % 2 == 0):
    n = int(input('Votre nombre:'))



print(">>>> break et continue:")

prenom = 'sylvain'

for lettre in prenom:

    if lettre == 'y':
        continue 
    # force le passage à l'itération suivante -> la suite de la boucle
    # la suite de la boucle n'est pas exécutée


    if lettre == 'i':
        break

    print(lettre) # slva
