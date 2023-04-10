# CS466 - Cloud Computing Project
##Towards a Proactive Lightweight Serverless Edge Cloud for Internet-of-Things Applications

Install Eclipse Mosquitto broker from [here](https://mosquitto.org/download/).
Clone the repository
Run the following coomand:
```
pip install -r requirement.text
```
Open command shell as administrator
Cd to mosquitto
Run following command to start mosquitto broker:
```
net start mosquitto
```
Run following command to know the broker addresses:
```
netstat -a
```
Paste the broker address in variable 'broker_address' in paho_client.py file
Run the client:
```
python paho_client.py
```
