import glib
import dbus

from dbus.mainloop.glib import DBusGMainLoop
from pusher import api


def print_notification(bus, message):
    keys = ["app_name", "replaces_id", "app_icon", "summary", "body", "actions", "hints", "expire_timeout"]
    args = message.get_args_list()
	
    if len(args) == 8:
        notification = dict([(keys[i], args[i]) for i in range(8)])
        print notification["summary"], notification["body"]
        api.push(notification["summary"], notification["body"])


api = api.API()

loop = DBusGMainLoop(set_as_default=True)
session_bus = dbus.SessionBus()
session_bus.add_match_string("type='method_call',interface='org.freedesktop.Notifications',member='Notify',eavesdrop=true")
session_bus.add_message_filter(print_notification)

glib.MainLoop().run()