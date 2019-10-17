from kafka import KafkaProducer


class MyKafkaProducer:
    def __init__(self, topic):
        self.topic = topic

    def message(self, message):
        print("Message to send to the messagging tier: {} (topic={})".format(
            message, self.topic))
