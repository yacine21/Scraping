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

def addPricesEnds(prices):
    prices.sort()
    result = []
    for i in range(len(prices)):
        lastPrice = ((i == len(prices) -1) or ((prices[i+1][0],prices[i+1][1])  != (prices[i][0], prices[i][1])))
        end = None if lastPrice else prices[i+1][2]
        result.append((prices[i][0] ,prices[i][1] ,prices[i][2], end ,prices[i][3]))
    return result

def insert_prices(connection , prices):
    cursor = connection.cursor()
    statement ="INSERT INTO Price(stationId , productId , start, end , value) VALUES(%s,%s,%s,%s,%s);"
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
    return result

def insert_shortages(connection,shortages):
    cursor = connection.cursor()
    statement ="INSERT INTO Shortage(stationId , productId , start , end ) VALUES(%s,%s,%s,%s);"
    cursor.executemany(statement,shortages)
    connection.commit()


def closing(pdv_liste):
    result = []
    for pdv in pdv_liste:
        station_id = pdv.attrib['id']
        for fermeture in pdv.findall('fermeture'):
            if len(fermeture.attrib)==0: continue
            type = fermeture.attrib['type']
            start =fermeture.attrib['debut']
            end = fermeture.attrib['fin']
            if end == "": end = None
             
            result.append((station_id, type , start , end)) 
    return result

def insert_closing(connection,closing):
    cursor = connection.cursor()
    statement ="INSERT INTO Closing(stationId , type , start , end ) VALUES(%s,%s,%s,%s);"
    cursor.executemany(statement,closing)
    connection.commit()






