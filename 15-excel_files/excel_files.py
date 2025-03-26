# 2 modules à installer
# pip install pandas
# pip install openpyxl

# Pandas est le module de réference dans l'analyse de données
# Il contient 2 types de données:
# serie: tableau à 1 seule dimension -> 1 colonne d'une table
# dataframe: table avec des lignes et des colonnes
# plus toutes les permettant de les manipuler

import pandas as pd

print(">>>>> Créer un dataframe:")

#sheet_name: choisir l'onglet
#usecols: choisir les colonnes

tab1 = pd.read_excel('15-excel_files/data.xlsx', sheet_name='tab1', usecols='A:C,E')
print(tab1)

print(tab1.dtypes) # afficher le type de contenu dans chaque colonne

print(">> Afficher une colonne:")
#2 syntaxes
print(tab1.age)
print(tab1['age'])

print(">>> Afficher le contenu d'une cellule:")

print(tab1.age[0]) # index des cellules commence à 0



print(">>>> Modifier le contenu d'une cellule:")

tab1.at[0, 'age'] = 42 # index 0 de colonne age
print(tab1)

print(">>>> Modifier toutes les cellules d'une colonne:")
print(tab1.age * 2)
print(tab1)

# créer un dictionnaire
d = {
    'age': tab1.age[0]
}

print(">>> filtres:")

condition = tab1.age >= 42
print(tab1[condition])

print('>>>>>>>>>>>>>>>>> Plusieurs fichiers excel:')

tab2 = pd.read_excel('15-excel_files/data.xlsx', sheet_name='tab2', usecols='A:C,E')

tab1_tab2 = pd.concat([tab1, tab2], ignore_index= False)
print(tab1_tab2)

tab1_tab2.to_excel('15-excel_files/result.xlsx', sheet_name='resultat', index=False)


print(">>> Calculs sur les colonnes numériques:")

print("Somme age: ", tab1.age.sum())
print("Moyenne age: ", tab1.age.mean())
print("Age min: ", tab1.age.min())
print("Age max: ", tab1.age.max())
condition = tab1.sexe == 'F'

print(tab1[condition].count())

tab1.to_xml('15-excel_files/out.xml')
tab1.to_csv('15-excel_files/out.csv')
d = tab1.to_dict()

print(d)

print(">>>>>>>>> Formules Excel avec openpyxl:")

from openpyxl import load_workbook

wb = load_workbook('15-excel_files/test.xlsx') # charger le fichier excel
feuille = wb['tab1'] # choisir l'onglet

nombre_de_lignes = len(list(feuille.rows))

if str(feuille['B' + str(nombre_de_lignes)].value) == 'Somme age':
    feuille.delete_rows(nombre_de_lignes, 1) # suppression de la cellule (ligne, colonne)
    feuille['B'+ str(nombre_de_lignes)] = 'Somme age'
    feuille['C'+ str(nombre_de_lignes)] = '=SUM(C2:C'+str(nombre_de_lignes - 1)+')'

else:
    # si ligne inexistante
    feuille['B'+ str(nombre_de_lignes + 1)] = 'Somme age'
    feuille['C'+ str(nombre_de_lignes + 1)] = '=SUM(C2:C'+str(nombre_de_lignes)+')'

wb.save('15-excel_files/test.xlsx')





