def prices(pdv_list):
    result = []
    for pdv in pdv_list:
        station_id = pdv.attrib['id']
        for prix in pdv.findall('prix'):
            if len(prix.attrib) == 0:continue
            product_id = prix.attrib['id']
            date = prix.attrib['maj']
            value = float(prix.attrib['valeur'])/1000
            result.append((station_id , product_id , date , value))
    return result

def insert_prices(connection , prices):
    cursor = connection.cursor()
    statement ="INSERT INTO Price(stationId , productId , date , value) VALUES(%s,%s,%s,%s);"
    cursor.executemany(statement,prices)
    connection.commit()

def shortages(pdv_liste):
    result = []
    for pdv in pdv_liste:
        station_id = pdv.attrib['id']
        for shortage in pdv.findall('rupture'):
            if len(shortage.attrib)==0:continue
            product_id =int(shortage.attrib['id'])
            start =shortage.attrib['debut']
            end = shortage.attrib['fin']
            if end == "": end = None
             
            result.append((station_id, product_id , start , end)) 

def insert_shortages(connection,shortages):
    cursor = connection.cursor()
    statement ="INSERT INTO Shortage(stationId , productId , start , end ) VALUES(%s,%s,%s,%s);"
    cursor.executemany(statement,prices)
    connection.commit()


def closing(pdv_liste):
    result = []
    for pdv in pdv_liste:
        station_id = pdv.attrib['id']
        for fermeture in pdv.findall('fermeture'):
            if len(fermeture.attrib)==0: continue
            type = fermeture.attrib['type']
            start =shortage.attrib['debut']
            end = shortage.attrib['fin']
            if end == "": end = None
             
            result.append((station_id, type , start , end)) 

def insert_closing(connection,shortages):
    cursor = connection.cursor()
    statement ="INSERT INTO Closing(stationId , type , start , end ) VALUES(%s,%s,%s,%s);"
    cursor.executemany(statement,prices)
    connection.commit()






