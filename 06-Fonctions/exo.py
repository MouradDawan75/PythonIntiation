#1)

print(len('test')) # taille d'une chaine

def somme_liste(ensemble_entiers):

    somme = 0
    for e in ensemble_entiers:
        somme = somme + e

    return somme


lst = [10,5,45,10,55,44]

resultat = somme_liste(lst)
print(resultat)

#2)

def moyenne_liste(entiers):
    somme = somme_liste(entiers) # appelle de la fonction somme_liste()
    nb_elements = len(entiers) # len: fonction qui renvoie la taille d'une collection

    return somme / nb_elements


print(moyenne_liste(lst))

#3)
def table_multiplication(nombre:int, premier_multiple:int, dernier_multiple:int):
    for i in range(premier_multiple, dernier_multiple + 1):
        print(f'{nombre} x {i} = {nombre * i}')

table_multiplication(11,1,12)
table_multiplication(8,1,10)

#4)
while True:

    choix = input("""
    
        1 - Convertir heures en minutes
        2 - Convertir minutes en heures
        3 - Quitter
    
        Choisir une opération:

    """)

    if choix == '3':
        break

    if choix == '1':
        heures = int(input('Heures: '))
        print(f'{heures}h = {heures * 60}m')

    if choix == '2':
        minutes = int(input('Minutes: '))
        print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')

# Code optimisé:

from mes_fonctions import afficher_menu,choix2,choix1


while True:

    choix = afficher_menu()

    if choix == '3':
        break

    if choix == '1':
        choix1()

    if choix == '2':
        choix2()