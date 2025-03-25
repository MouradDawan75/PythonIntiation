def fonction1():
    print('fonction1..........')


# |__modules.py
# |__mypackage
# |_____init__.py
# |_____mesfonctions.py


# Si ce module est exécuté
if __name__ == '__main__':
    print('>>>>> code de mesfonctions....')
    print(__name__)
