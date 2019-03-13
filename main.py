import os
import dotenv
import mysql.connector 
import xml.etree.ElementTree as et
from service import *
#from product import *
from stations import *

def main():
    dotenv.load_dotenv()
    connection = mysql.connector.connect(
        host=os.getenv('dbHostname'), user = os.getenv('dbUser') , passwd = os.getenv('dbPass') , database=os.getenv('dbName')
    )

    base_path = os.path.dirname(os.path.realpath(__file__))
    xml_file = os.path.join(base_path,"data/PrixCarburants_annuel_2019.xml")
    tree = et.parse(xml_file)
    pdv_liste = tree.getroot()
    #print(get_services(connection))
    
    #insert_products(connection , products(pdv_liste))
    # print(get_products(connection))
    #print(get_stations(connection))
    # insert_stations(connection,stations(pdv_liste))
    station_services(pdv_liste,get_services(connection))

if __name__ == '__main__':
    main()


