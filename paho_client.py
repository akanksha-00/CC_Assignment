import time
import paho.mqtt.client as paho


broker_address = "broker_address"


#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

#create client object client1.on_publish = on_publish 
client= paho.Client("client-001") 

#Bind function to callback
client.on_message=on_message

#connect
print("connecting to broker ", broker_address)
client.connect(broker_address, port=1883)

#start loop to process received messages
client.loop_start() 

#subscribe
print("subscribing to topic bulb1")
client.subscribe("house/bulb1")
time.sleep(2)

#publish
print("publishing to topic bulb1")
client.publish("house/bulb1","on")
time.sleep(4)

#disconnect
client.disconnect() 

#stop loop
client.loop_stop() 