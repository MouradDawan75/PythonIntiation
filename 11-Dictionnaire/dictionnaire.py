# dict: est une collection non ordonnée qui fonctionne par association clé:valeur
# Dans un dictionnaire physique, le mot est la clé sa définition est la valeur
# Dans un dictionnaire les clés sont uniques

# dict vide:

d1 = {}
d2 = dict()

# un dictionnaire permet de regrouper les caractéristiques d'un objet

user = {
    'nom' : 'DUPONT',
    'prenom' : 'Jean',
    'age' : 65
}

# Affichez le nom:
print(user['nom'])
#print(user['Nom']) si clé inexistante: erreur

print(user.get('nom'))
print(user.get('Nom'))

# Créer de nouvelles clés:
user['contrat'] = 'CDD'

print(user)

user['contrat'] = 'CDI' # si clé existante: elle est écrasée
print(user)

# On peut aussi avoir des dict complèxes:

utilisateur = {
    'nom' : 'DUPONT',
    'prenom' : 'Jean',
    'age' : 65,
    'telephones': ['06060606','07070707'],
    'adresse': {
        'rue': '15 rue Machin',
        'code_postal': 75001
    }
}

# Afficher chaque num. de tél.:

for t in utilisateur.get('telephones'):
    print(t)

print(utilisateur.get('telephones'))

# Afficher la rue:
print(utilisateur.get('adresse').get('rue'))

print(">>>>>>>>>>>>>> Appelle d'un API Rest:")

# Web Service Rest - Api Rest: est une application web sans IHM, qui rnvoie du contenu JSON.
# Elle n'est pas limitée au format JSON, elle peut renvoyée du texte, du xml et du binaire.

# Api REST est un ensemble de ressources (images, article d'un journal...) où chaque 
# possède un ID (URI: Uniform Resource Identifier - endpoint), une méthode d'accès 
# GET,DELETE,PUT,POST et elle peut publique ou privée

# Toutes ces infos sont fournies dans la documentation de l'API

# En Python, il faut installer le module requests pour faire appel à des api.

# Pour installer des modules externes, on utilise le pip (destionnaire de modules externes)
# pip install nom_module
# pip uninstall nom_module
# pip list


import requests

URI = 'https://restcountries.com/v3.1/all'

#json(): garantir un contenu json en réponse

reponse = requests.get(URI).json()

#print(reponse) -> c'est une liste de dict

country = input('Votre pays: ')

for pays in reponse:
    if country == pays.get('name').get('common'):
        print(f"Name: {pays.get('name').get('common')} - Capitale: {pays.get('capital')} - Population: {pays.get('population')}")
