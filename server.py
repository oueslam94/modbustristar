import os
from flask import Flask,jsonify, request, render_template, Response
from flask_restful import Resource, Api
import json
import socket

def findip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    with open('ReactApp/joesapp/src/Components/ip.json', 'w') as fp:
        json.dump({"ip": ip}, fp)
    return ip

app = Flask(__name__)
api = Api(app)


@app.route('/rawdata', methods=['GET'])
def yourMethod():
    with open('ReactApp/joesapp/src/Components/tristar.json') as json_data:
        data = json.load(json_data)
        # print(data)
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    ip = findip()
    app.run(ip,debug=True)
