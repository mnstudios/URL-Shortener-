import pyshorteners as sh
import json
from flask import Flask,request, jsonify



app = Flask(__name__,template_folder='template')
app.debug = True


@app.route('/create', methods=['post'])
def create():
    data = request.get_json()
    url=data["url"]
    s = sh.Shortener()
    print('Data Received: "{data}"'.format(data=url))
    tiny = s.tinyurl.short(url)
    return "Request Processed.\n"


@app.route('/edit', methods=['post'])
def edit():
    data = request.get_json()
    short=data["short"]
    url=data["url"]
    s = sh.Shortener()
    s = sh.Shortener()
    print('Data Received: "{data}"'.format(data=url))
    tiny = s.tinyurl.short(url)

    return "Request Processed.\n"

@app.route('/<int:id>', methods=['get'])
def get(id):
    print(id)
    return "Request Processed.\n"


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=4001)
   
