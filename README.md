To Run this application you must download the mosquitto broker and the add these lines to the mosquitto.conf file :
listener 4000
protocol websockets

listener 1883
protocol mqtt

allow_anonymous true

and after that run the mosquitto broker using this command :
mosquitto.exe -c -v mosquitto.conf.

 
 
# DashDeploy
