def services(pdv_liste):
    services = set() # non duplicated list
    for pdv in pdv_liste:
        for service in pdv.find('services'):
            services.add(service.text)
    return services

def insert_services(connection, services):
    data = []
    for service in services:
        data.append((service, ))
        cursor = connection.cursor()
        statement = "INSERT INTO Service(name) VALUES(%s);"
        cursor.executemany(statement, data)
        connection.commit()

def get_services(connection):
    cursor = connection.cursor()
    statement ="SELECT * FROM Service;"
    cursor.execute(statement)
    column_names = [column_desc[0] for column_desc in cursor.description]
    return [dict(zip(column_names,row)) for row in cursor]

def get_service_id(services , text):
    for service in services:
        if service['name'] == name:
            return service['id']
    return None


def station_services(pdv_liste,services):
        result = []
        for pdv in pdv_liste:
                station_id = pdv.attrib(['id']
                for service in pdv.find('services').findall('service'):
                        name = service.text
                        service_id = get_service_id(services , name)
                        result.append((station_id, service_id))
        return result

