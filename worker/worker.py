import paho.mqtt.client as mqtt
from db.client import connect, commit_message
import logging
import json
import os


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("thndr-trading")

def on_message(client, userdata, msg):
    logging.warning(str(msg.payload))
    message = json.loads(msg.payload)
    commit_message(message)


def main(): 
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(os.environ['VERNEMQ_HOST'], 1883, 60)
    client.loop_forever()


if __name__=="__main__":
    main()

