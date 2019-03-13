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