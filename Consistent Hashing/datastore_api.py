from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from hashids import Hashids
from flask_restful import reqparse
from flask_restful import reqparse, abort, Api, Resource

import  sys


app = Flask(__name__)
api = Api(app)
entries = []
content = {
                "num_entries" : len(entries),
                "entries" :
                    entries
        }    

#parser = reqparse.RequestParser()
#parser.add_argument('hash_key', type =str, help ='hash_key')
#parser.add_argument('hash_value', type=str, help ='hash_value')

class Datastore(Resource):
    def get(self):
        
        return content, 200
    
    def post(self):
        data = request.get_json(force=True)
        xxxx = data['xxxx']
        return jsonify({'xxxx':xxxx}), 201
        '''args = parser.parse_args()
        entries.append({args['hash_key']:args['hash_value']})
        content['num_entries'] = len(entries)
        return content, 201
        '''

api.add_resource(Datastore, '/api/v1/entries')

if __name__ == '__main__':
    app.run(port=5000,debug=True)