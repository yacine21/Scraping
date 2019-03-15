import os
import dotenv
import mysql.connector 
import xml.etree.ElementTree as et
from service import *
from product import *
from stations import *
from price import *
import sys

def clear_db(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Closing;")
    cursor.execute("DELETE FROM Price;")
    cursor.execute("DELETE FROM Shortage;")
    cursor.execute("DELETE FROM StationService;")
    cursor.execute("DELETE FROM Station;")
    cursor.execute("DELETE FROM Product;")
    cursor.execute("DELETE FROM Service;")

def main():
    dotenv.load_dotenv()

    connection = mysql.connector.connect(
        host=os.getenv('dbHostname'), user = os.getenv('dbUser') , passwd = os.getenv('dbPass') , database=os.getenv('dbName')
    )

    #base_path = os.path.dirname(os.path.realpath(__file__))
    #xml_file = os.path.join(base_path,"data/PrixCarburants_annuel_2019.xml")
   
    tree = et.parse(sys.argv[1])
    pdv_liste = tree.getroot()
    clear_db(connection)
    insert_services(connection ,services(pdv_liste))
    insert_products(connection ,products(pdv_liste))
    insert_stations(connection ,stations(pdv_liste))
    insert_station_services(connection, station_services(pdv_liste,get_services(connection)))
    insert_prices(connection, prices(pdv_liste))
    insert_shortages(connection,shortages(pdv_liste))
    insert_closing(connection, closing(pdv_liste))

    connection.commit()

    
if __name__ == '__main__':
    main()


