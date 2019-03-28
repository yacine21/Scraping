from flask import Flask, jsonify, jsonify
from flask_cors import CORS
from flaskext.mysql import MySQL
import os 
import dotenv
from service import get_services

dotenv.load_dotenv()
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = os.getenv('dbHostname')
app.config['MYSQL_DATABASE_USER'] = os.getenv('dbUser')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('dbPass')
app.config['MYSQL_DATABASE_DB'] = os.getenv('dbName')
mysql.init_app(app)
CORS(app)


@app.route('/products', methods=['GET'])
def products():
    cursor = mysql.get_db().cursor()
    statement = "SELECT * FROM Product;"
    cursor.execute(statement)
    column_names = [column_desc[0] for column_desc in cursor.description]
    return jsonify([dict(zip(column_names, row)) for row in cursor])



@app.route('/services', methods=['GET'])
def services():
    cursor = mysql.get_db().cursor()
    statement = "SELECT * FROM Service;"
    cursor.execute(statement)
    column_names = [column_desc[0] for column_desc in cursor.description]
    return jsonify([dict(zip(column_names, row)) for row in cursor])


@app.route('/departements/prices/<int:productId>/<string:date>', methods=['GET'])
def function(productId,date):
    cursor = mysql.get_db().cursor()
    statement = """
                SELECT LEFT(postalCode,2) as departement , AVG(value) as average FROM Price
                INNER JOIN Station ON Price.stationId = Station.id
                WHERE Price.productId = %(productId)s
                    AND NOT EXISTS (SELECT * FROM Shortage 
                    WHERE Shortage.stationId = Station.id 
                        AND Shortage.productId = %(productId)s
                        AND Shortage.start <= %(date)s
                        AND (Shortage.end IS NULL OR Shortage.end >= %(date)s))
                AND NOT EXISTS (SELECT * FROM Closing
                    WHERE Closing.stationId = Station.id
                    AND Closing.start <= %(date)s
                    AND (Closing.end IS NULL OR Closing.end >= %(date)s))
                GROUP BY departement
                ORDER BY departement
    
    
    """
    cursor.execute(statement , {'productId': productId , 'date':date})
    column_names = [column_desc[0] for column_desc in cursor.description]
    return jsonify([dict(zip(column_names, row)) for row in cursor])



# @app.route('/stations/prices/<int:productId/<string:date>/<string:lat/<string:long>/<int:distance>/<int:limit> ')

# def function2(productId, date, lat, long, distance, limit):
#     cursor = mysql.get_db().cursor()
#     statement = """ 
#                     SELECT LEFT(postalCode,2) as departement, AVG(value) as average FROME Price
#                     INNER JOIN Station On Price.stationId = Station.id
#                     WHERE Price.productId = %(productId)s
#                         AND Price.start <= %(date)s AND Price.end > %(date)s
#                         AND NOT EXISTS (SELECT * FROM Shorateg
#                                             WHERE Shortage.stationId = Station.id
#                                              AND Shortage.productId = %(productID)s
#                                              AND Shortage.start <= %(date)s
#                                              AND (Shortage.end IS NULL OR Shortage.end >= %(date)s))
#                         AND NOT EXISTS (Select * From Closing
#                                             WHERE Closing.stationId = Station.id
#                                                 AND Closing.start <= %(date)s
#                                                 AND (Closing.end IS NULL OR Closing.end >= %(date)s))
#                     GROUP BY departement
#                     ORDER BY departement;"""
#     cursor.execute(statement , {'productId': productId , 'date':date})
#     column_names = [column_desc[0] for column_desc in cursor.description]
#     return jsonify([dict(zip(column_names, row)) for row in cursor])
