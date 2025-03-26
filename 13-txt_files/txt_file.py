# 1- Construction du chemin
chemin_fichier = 'c:\\......' # à éviter

import os # facilite la gestion des paths

print(__file__) # c:\......\txt_files.py

chemin_dossier_en_cours = os.path.dirname(__file__) # c:\....\13-txt_files

#chemin_fichier = chemin_dossier_en_cours +'\demo.txt'

chemin_fichier = os.path.join(chemin_dossier_en_cours,'demo.txt')
# join: génère un chemin selon l'os utilisé

# 2- Appelle de a fonction open:
# paramètres:
# - chemin
# - mode d'accès: r: read, w: write, a: append
# En mode w et a si le fichier n'existe pas, la fct le crée
# - encodage: 'utf-8'

# Obligation: une ressouce doit être libérée à la fin de son utilisation

#Ecriture
flux = open(chemin_fichier, 'a', encoding='utf-8')
flux.write('\nceci est le contenu du fichier')
flux.close()

#Lecture
flux = open(chemin_fichier,'r', encoding='utf-8')
contenu = flux.read()
flux.close()

print(contenu)

# Context Manager (with resource): s'occupe de fermer la ressource à la fin

print('>>>>>>>>>>>> Context Manager <<<<<<<<<<<<<<<<<')

with open(chemin_fichier,'r', encoding='utf-8') as flux:
    print(flux.read()) # vous arrivez à la fin du fichier. La prochaine lecture n'aura ligne à lire
    #flux.close() - exécuté par le with
    print("*********************************")
    flux.seek(0) # seek: permet de déplacer le curseur de lecture dans le fichier
    #flux.seek(5) # renvoie le 6ème caractère
    #whence = 0: partir du début du fichier
    #whence = 1: partir de la position actuelle du curseur
    #whence = 2: partir de la fin du fichier
    print(flux.read())
    print('**********************************')

#print(flux.read())

print('>>>>>>>Test des fonctions de lecture et écriture:')

from filetool import lecture_fichier_texte,ecriture_fichier_texte

chemin_test = os.path.join(chemin_dossier_en_cours, 'test.txt')

ecriture_fichier_texte(chemin_test, 'contenu du fichier......', mode_ajout=True)

print(lecture_fichier_texte(chemin_test))

print(">>>>>> Module OS:")

print(os.getcwd()) # renvoie le chemin du dossier principal (dossier du projet)
 
print(os.path.exists(chemin_fichier))

# Créer des répertoires:

chemin_dossier = os.path.join(chemin_dossier_en_cours, 'rep')

# os.mkdir(): pour 1 seul dossier
# os.makedirs(): pour des sous répertoires
if os.path.exists(chemin_dossier):
    print('existe déjà')
else:
    os.mkdir(chemin_dossier)
    print('dossier crée')

for f in os.listdir(chemin_dossier_en_cours):
    print(f)

# Exo: à partir du dossier en cours, lire tous les fichiers .txt et insérer le contenu 
# dans un nouveau fichier new.txt
# résultat attendu:
# >>>>>>>>>>>>>>>> nom fichier lu
# contenu du fichier

contenu = '' # contient le texte final à insérer dans le fichier new.txt

for f in os.listdir(chemin_dossier_en_cours):
    # vérifier l'extension
    if f.endswith('.txt'):
        #f ne contient que le nom du fichier -> on doit construire le chemin complet
        chemin = os.path.join(chemin_dossier_en_cours, f)
        contenu = contenu +'>>>>>>>>>> fichier: '+f+'\n'+ lecture_fichier_texte(chemin_fichier)+'\n'

if contenu != '':
    chemin_fichier_new = os.path.join(chemin_dossier_en_cours, 'new.txt')
    ecriture_fichier_texte(chemin_fichier_new, contenu)

else:
    print('Aucun fichier trouvé......')
        



