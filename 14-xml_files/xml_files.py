import xml.dom.minidom

# Etape 1: parser le fichier xml

xml_doc = xml.dom.minidom.parse('14-xml_files/new_packages.xml')

# Afficher le root element
root = xml_doc.documentElement
print(root)

# get all packages
xml_doc.getElementsByTagName('package')
