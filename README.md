Pusher
====

Pusher is a python library for [Pushbullet](https://www.pushbullet.com/) .

Usage
---
Push note
```
from pusher import api

api = api.API()
api.push("My Body", "My Title")
```

Push file

```
from pusher import api

api = api.API()
api.push_file("path/to/file", "My Body")
```

See the [examples](https://github.com/ziggy42/Pusher/tree/master/examples) and the [official docs](https://docs.pushbullet.com/) for more details.