# fonction d'écriture dans fichier

def ecriture_fichier_texte(chemin_fichier: str, contenu: str, mode_ajout: bool = False):
    """Fonction d'écriture dans un ficher texte. Par défaut, utilise le mode w.

    Args:
        chemin_fichier (str): chemin absolut du fichier. Ex: c:\\dossier\\notes.txt
        contenu (str): texte à insérer dans le fichier
        mode_ajout (bool, optional): mettre à True pour un accès en mode append.
    """
    # mode d'accès par défaut
    mode_acces = 'w'
    if mode_ajout == True:
        mode_acces = 'a'
        contenu = '\n'+contenu # faire un retour à la ligne avant d'insérer le contenu

    with open(chemin_fichier,mode_acces, encoding='utf-8') as flux:
        flux.write(contenu)


# fonction de lecture d'un fichier

def lecture_fichier_texte(chemin_fichier: str):
    """Fonction de lecture d'un fichier texte.

    Args:
        chemin_fichier (str): Chemin absolut du fichier à lire. Ex: c:\\dossier\\notes.txt

    Returns:
        _type_: renvoie le contenu du fichier.
    """
    with open(chemin_fichier, 'r', encoding='utf-8') as flux:
        contenu = flux.read()


    return contenu

# Génération de la documentation technique:
# Dans Vs Code: installez l'extension autodocstring