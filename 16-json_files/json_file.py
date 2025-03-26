import json
import os

# Contrairement à un fichier texte, un fichier json en plus du texte contient des données
# des listes, des types numériques.......

chemin_dossier = os.path.dirname(__file__)
chemin_json = os.path.join(chemin_dossier, 'users.json')

# Lecture JSON

with open(chemin_json, 'r', encoding='utf-8') as flux:
    contenu = json.load(flux) # c'est liste de dictionnaires

for user in contenu:
    print(f"Name: {user.get('name')} - Email: {user.get('email')} - Latitude: {user.get('address').get('geo').get('lat')}")


# Ecriture JSON:

chemin_sortie = os.path.join(chemin_dossier, 'sortie.json')

# Construction du contenu: liste de dict:

lst = []

for user in contenu:

    d = {
        "name": user.get('name'),
        "email": user.get('email'),
        "latitude" : user.get('address').get('geo').get('lat')
        }

    lst.append(d)


with open(chemin_sortie, 'w', encoding='utf-8') as flux:
    # Contenu à insérer:
    # Soit un dict, soit une liste de dict
    # ensure_ascii=True - tous les caractères non ascii seront ignorés

    json.dump(lst, flux, indent=4, ensure_ascii=False) 

