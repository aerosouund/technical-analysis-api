import paho.mqtt.client as mqtt
import psycopg2

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("thndr-trading")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # parse the incoming JSON message
    message = json.loads(msg.payload)
    stock_id = message['stock_id']
    name = message['name']
    price = message['price']
    availability = message['availability']
    timestamp = message['timestamp']

    # connect to the PostgreSQL database
    conn = psycopg2.connect(host="localhost", database="your_database_name", user="your_username", password="your_password")
    cur = conn.cursor()

    # insert the message into the table
    cur.execute("INSERT INTO stock_data (stock_id, name, price, availability, timestamp) VALUES (%s, %s, %s, %s, %s)", (stock_id, name, price, availability, timestamp))
    conn.commit()

    # close the database connection
    cur.close()
    conn.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
