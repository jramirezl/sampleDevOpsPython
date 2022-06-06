from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello1'


@app.route('/barrios', methods=['GET'])
def get_barrios():
    url = 'https://6285638196bccbf32d622180.mockapi.io/api/v1/barrios'
    response = requests.get (url, {}, timeout=5 )
    return  {"barrios": response.json() }


@app.route('/barrios', methods=['POST'])
def add_barrios():
    barrios = {"barrios": [{"nombre": request.json['nombre'], "ubicacion": request.json['ubicacion']}]}
    return barrios



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)