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
        statement = "INSERT INTO Service(name) VALUES(%s)"
        cursor.executemany(statement, data)
        connection.commit()