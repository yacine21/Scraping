def products(pdv_liste):
    products = set() 
    for pdv in pdv_liste:
        for price in pdv.findall('prix'):
            if len(price.attrib)==0: continue
            products.add((int(price.attrib['id']), price.attrib['nom'])
    return list(products)
    
def insert_products(connetion , products):
    cursor = connetion.cursor()
    statement = "INSERT INTO Product(id, name) VALUES(%s,%s);"
    cursor.executemany(statement,products)
    connetion.commit()

def get_products(connection):
    cursor = connection.cursor()
    statement ="SELECT * FROM Product;"
    cursor.execute(statement)
    column_names = [column_desc[0] for column_desc in cursor.description]
    return [dict(zip(column_names,row)) for row in cursor]