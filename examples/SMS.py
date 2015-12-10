from pusher import api

data = {
    "conversation_iden": "+39 123456789",
    "message": "Hello!",
    "package_name": "com.pushbullet.android",
    "source_user_iden": "useriden",
    "target_device_iden": "deviceiden",
    "type": "messaging_extension_reply"
}

api = api.API()
api.send_ephemeral(data)