def stations(pdv_list):
    stations = []
    for pdv in pdv_list:
        id = pdv.attrib['id']
        postalcode = pdv.attrib['cp']
        position = pdv.attrib['pop']
        address = pdv.find('adresse').text
        city = pdv.find('ville').text
        if city is None:
            city = address
        latitude = pdv.attrib['latitude']
        longitude = pdv.attrib['longitude']
        if latitude == "" or longitude =="":
            latitude=0
            longitude=0
        else:
            latitude = float(latitude) / 100000
            longitude = float(longitude) / 100000



        lat = pdv.attrib['latitude']
        lon = pdv.attrib['longitude']
        automate = pdv.find('horaires').attrib['automate-24-24'] == '1'
        stations.append((id, postalcode,position, address,city, lat,lon,automate))
    return stations


def insert_stations(connection , stations):
    cursor = connection.cursor()
    statement ="INSERT INTO Station(id,postalCode, position, address, city , gps , automate) VALUES(%s,%s,%s,%s,%s,POINT(%s,%s),%s);"
    cursor.executemany(statement, stations)
    connection.commit()

def get_stations(connection):
    cursor = connection.cursor()
    statement ="SELECT * FROM Station;"
    cursor.execute(statement)
    column_names = [column_desc[0] for column_desc in cursor.description]
    return [dict(zip(column_names,row)) for row in cursor]
