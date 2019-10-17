import paho.mqtt.client as mqtt

from kafka_producer import MyKafkaProducer

KAFKA_TOPIC = "test"

# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("gps")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):

    with open("./data/data.txt", 'a') as archivo:
        archivo.write(msg.topic+" "+str(msg.payload) + "\n")

    # Send the message to kafka
    kafka.message(msg)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

kafka = MyKafkaProducer(KAFKA_TOPIC)

client.connect("localhost", 8000, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
