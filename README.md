#Pusher


Pusher is  a simple, command-line client for [Pushbullet](https://www.pushbullet.com/) .

Usage
--
Find your access token [here](https://www.pushbullet.com/account) 
```
usage: pusher [-h]
              [-sp MSG | -spd MSG DEVICE_ID | -p | -pd DEVICE_ID | -i | -l | -pf FILE_NAME]
              AccessToken

Pusher is a PushBullet command line client

positional arguments:
  AccessToken

optional arguments:
  -h, --help          show this help message and exit
  -sp MSG             Simple Push
  -spd MSG DEVICE_ID  Simple Push to a selected device
  -p                  Push
  -pd DEVICE_ID       Push to a selected device
  -i                  Get user info
  -l                  Get device list
  -pf FILE_NAME       Upload file
```
