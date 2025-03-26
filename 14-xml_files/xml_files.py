import xml.dom.minidom
from xmltool import copie_xml, add_xml_root_tag

chemin_source = '14-xml_files/new_packages.xml'
chemin_copie = '14-xml_files/copie.xml'
copie_xml(chemin_source, chemin_copie)
add_xml_root_tag(chemin_copie)

# Etape 1: parser le fichier xml

xml_doc = xml.dom.minidom.parse('14-xml_files/new_packages.xml')

# Afficher le root element
root = xml_doc.documentElement
print(root)

# get all packages
package_list = xml_doc.getElementsByTagName('package')


for package in package_list:

    #extraire les attributs xml
    package_id = package.getAttribute('id')

    #extraire les tags
    description = package.getElementsByTagName('description')[0].childNodes[0].data
    destination = package.getElementsByTagName('destination')[0].childNodes[0].data
    payment_refund = package.getElementsByTagName('payment')[0].getElementsByTagName('refund')[0].childNodes[0].data

    print('ID:', package_id)
    print('Description:', description)
    print('Destination:',description)
    print('Payment refund:', payment_refund)


import xml.etree.ElementTree as ET

tree = ET.parse('14-xml_files/new_packages.xml')

root = tree.getroot()
print(root)

print(">>>>>>> Modifications:")

for package in root.iter('package'):
    price = int(package.find('price').text)
    refund = package.find('payment/refund').text.strip()

    # find(nom_tag): pour cibler les tags
    # attrib['nom_attribut]: cibler les attributs
    print(package.attrib['id'])
    if price > 4000 and refund =='no':
        new_price = 45000
        package.find(price).text = str(new_price)

        # valider les modifications dans le fichier
        tree.write('14-xml_files/new_packages.xml')
       



# pip install pandas
# pip install openpyxl -> nécessaire pour les fichiers excel

