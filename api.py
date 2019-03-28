from flask import Flask, jsonify
from service import get_services
app = Flask(__name__)


def main():
    dotenv.load_dotenv()
    connection = mysql.connector.connect(
    host=os.getenv('dbHostname'), user = os.getenv('dbUser') , passwd = os.getenv('dbPass') , database=os.getenv('dbName'))

@app.route("/")
def serve():
    return jsonify({"data":"data" , "some data":"other data"})

if __name__ == "__main__":
    app.run(debug=True)