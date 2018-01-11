import os
from flask import Flask,jsonify, request, render_template, Response
from flask_restful import Resource, Api
import json



app = Flask(__name__)
api = Api(app)


@app.route('/rawdata', methods=['GET'])
def yourMethod():
    response = jsonify({'some': 'data'})
    with open('ReactApp/joesapp/src/Components/tristar.json') as json_data:
        data = json.load(json_data)
        # print(data)
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=False)
