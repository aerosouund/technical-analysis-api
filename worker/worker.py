import paho.mqtt.client as mqtt
from db.client import connect
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("thndr-trading")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # parse the incoming JSON message
    message = json.loads(msg.payload)
    commit_message(message)


def main(): 
    session = connect()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)
    client.loop_forever()


if __name__=="__main__":
    main()

