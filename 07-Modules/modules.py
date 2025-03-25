# Syntaxes de l'import

import math

math.sqrt(16)

# On peut aussi modifier le nom du module importé: définir un alias

import random as rd

rd.randint(1,10)

# On peut aussi importer des éléments spécifiques à partir d'un module

from math import sqrt,pow

sqrt(10)
pow(10,2)

# On peut aussi modifier le nom de l'élément spécifique importé

from math import sqrt as racine_carree

racine_carree(25)

# Un module est un fichier .py contenant généralement des fonctions, des classes ou des constantes
# Un package est répertoire contenant des modules.

# Obligation: le nom d'un package ou d'un module doit être miniscules, sans espaces ni undescore et doit 
# commencé par une lettre 

# Pour convertir un répertoire en package, on doit ajouter le fichier __init__.py qu'on
# peut laisser vide.

# Python < 3.3: __init__.py est obligatoire
# Python >= 3.3: __init__.py est optionnel mais il est recommandé de le générer pour des raisons
# de compatibilité

# Appelle de fonction1:

#Option1: importer tout le module
#from mypackage import mesfonctions

#Option2: importer la fonction1
from mypackage.mesfonctions import fonction1

#fonction1()
# Un module importé est tout le temps exécuté

# Le fichier __init__.py est exécuté en premier lors d'un import

# pour un module exécuté: __name__ == '__main__'
# pour un module importé: __name__ == 'nom module importé'

from mypackage.mesconstantes import SERVER,PORT,USER,PASSWORD

# Lecture des variables d'environnment de windows: redémarrer windows

import os

print(os.getenv('FORMATION'))

#os.system('cls') # clear screen

import getpass

password = getpass.getpass('Votre mot de passe: ') # permet de masquer les caractères saisis
print(password)