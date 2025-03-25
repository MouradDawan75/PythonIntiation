def convertir_heures_en_minutes(heures):
    print(f'{heures}h = {heures * 60}m')

def convertir_minutes_en_heures(minutes):
    print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')

def afficher_menu():

    choix = input("""
    
        1 - Convertir heures en minutes
        2 - Convertir minutes en heures
        3 - Quitter
    
        Choisir une opération :

    """)

    return choix

def choix1():
     heures = int(input('Heures: '))
     convertir_heures_en_minutes(heures)


def choix2():
    minutes = int(input('Minutes: '))
    convertir_minutes_en_heures(minutes)