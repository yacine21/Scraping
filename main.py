import os
import socket
import xml.etree.ElementTree as et
import mysql.connector 

#host = socket.gethostbyname('dbs-perso.luminy.univmed.fr')
db = mysql.connector.connect(
    host ='139.124.69.90',
    database='o17028459',
    user='o17028459',
    passwd='fijxCh6t'
)
print(db)
base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path,"data/sample.xml")
tree = et.parse(xml_file)
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
# new_product = et.SubElement(root ,"product",attrib={"id":"3"})
# new_product_name =et.SubElement(new_product,"name")
# new_product_description =et.SubElement(new_product,"description")
# new_product_cost =et.SubElement(new_product,"cost")
# new_product_shipping =et.SubElement(new_product,"shipping")

# new_product_name.text = "Vendetta Mask"
# new_product_description.text = "Vendetta Mask like Anonymous"
# new_product_cost.text = "8"
# new_product_shipping.text ="4"
# tree.write(xml_file)

# for child in root:
#     for el in child:
#         print(el.tag , ":" , el.text)

