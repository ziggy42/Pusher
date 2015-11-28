#Pusher


Pusher is  a simple, command-line client for [Pushbullet](https://www.pushbullet.com/) .

Usage
--
* Actions:
```
usage: pusher.py [-h] {push,list,user} ...

Pusher is a PushBullet command line client

positional arguments:
  {push,list,user}
    push            push command
    list            list command
    user            display user info

optional arguments:
  -h, --help        show this help message and exit
```

* Push
```
usage: pusher.py push [-h] [-f path] body [title]

positional arguments:
  body        the main content of the push
  title       the title of the push

optional arguments:
  -h, --help  show this help message and exit
  -f path     file

```

* List
```
usage: pusher.py list [-h] [-d]

optional arguments:
  -h, --help  show this help message and exit
  -d          list devices
```

* User
```
usage: pusher.py user [-h]

optional arguments:
  -h, --help  show this help message and exit
```
