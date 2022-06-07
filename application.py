from flask import Flask
import requests
import os

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello'


@app.route('/barrios', methods=['GET'])
def get_barrios():
    url = 'https://6285638196bccbf32d622180.mockapi.io/api/v1/barrios'
    response = requests.get (url, {}, timeout=5 )
    return  {"barrios": response.json() }


@app.route('/barrios', methods=['POST'])
def add_barrios():
    barrios = {"barrios": [{"nombre": request.json['nombre'], "ubicacion": request.json['ubicacion']}]}
    return barrios


port = os.environ.get("PORT", 5000)
print('get port %d' % port)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)



