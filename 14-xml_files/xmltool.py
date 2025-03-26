
import shutil

# Fonction de copie de fichier xml

def copie_xml(chemin_source, chemin_destination):
    shutil.copy(chemin_source,chemin_destination)


# Fonction d'ajout du root tag

def add_xml_root_tag(chemin_source_xml):
    lignes = []
    with open(chemin_source_xml, 'r') as flux:
        lignes = flux.readlines()
        lignes.insert(1,'<root>') # ajout de ligne 2
        lignes.append('</root>')
        

    with open(chemin_source_xml,'w') as flux:
        flux.writelines(lignes)