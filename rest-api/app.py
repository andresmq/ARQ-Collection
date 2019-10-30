from flask import Flask
from flask_restful import Api, Resource, reqparse
from kafka import KafkaProducer
import json

app = Flask(__name__)
api = Api(app)
producer = KafkaProducer(bootstrap_servers=["localhost:9092"])


class GpsData(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("timestamp")
        parser.add_argument("id_vehiculo")
        parser.add_argument("latitud")
        parser.add_argument("longitud")
        parser.add_argument("velocidad")

        args = parser.parse_args()

        # self.save_to_file(args)
        self.send_to_kafka(args)

        return "ok", 200

    def save_to_file(self, msg):
        with open("./data/data.txt", 'a') as archivo:
            content = []
            for k, v in msg.items():
                content.append("{0}: {1}".format(k, v))
            archivo.write(" | ".join(content) + "\n")

    def send_to_kafka(self, msg):
        content = []
        for k, v in msg.items():
            content.append("{0}: {1}".format(k, v))
        msg = " | ".join(content)
        producer.send("gps", bytes(msg, 'utf-8'))


api.add_resource(GpsData, "/gps")
app.run(debug=True)
