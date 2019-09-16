from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

class GpsData(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("timestamp")
        parser.add_argument("id_vehiculo")
        parser.add_argument("latitud")
        parser.add_argument("longitud")
        parser.add_argument("velocidad")

        args = parser.parse_args()

        self.save_to_file(args)
        return "ok", 200


    def save_to_file(self, msg):
        with open( "./data/data.txt", 'a') as archivo:
            content = []
            for k, v in msg.items():
               content.append("{0}: {1}".format(k,v))
            archivo.write(" | ".join(content) + "\n")


api.add_resource(GpsData, "/gps")
app.run(debug=True)

