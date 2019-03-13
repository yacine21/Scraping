import os
import dotenv
import mysql.connector 
import xml.etree.ElementTree as et
from service import services, insert_services
def main():
    dotenv.load_dotenv()
    connection = mysql.connector.connect(
        host=os.getenv('dbHostname'), user = os.getenv('dbUser') , passwd = os.getenv('dbPass') , database=os.getenv('dbName')
    )
    print(connection)

    base_path = os.path.dirname(os.path.realpath(__file__))
    xml_file = os.path.join(base_path,"data/PrixCarburants_annuel_2019.xml")
    tree = et.parse(xml_file)
    pdv_liste = tree.getroot()
    
    insert_services(connection,services(pdv_liste))

if __name__ == '__main__':
    main()


