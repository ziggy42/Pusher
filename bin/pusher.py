#!/usr/bin/env python3
import argparse

from pusher import api


pusher_api = api.API()

parser = argparse.ArgumentParser(description='Pusher is a PushBullet command line client')
subparsers = parser.add_subparsers(dest='cmd')
subparsers.required = True

# Push
parser_push = subparsers.add_parser('push', help='push command')
parser_push.add_argument('body', help='the main content of the push')
parser_push.add_argument('title', help='the title of the push', nargs='?')

# List
parser_list = subparsers.add_parser('list', help="list command")
parser_list.add_argument('-d', action='store_true', help="list devices")

# User
parser_list = subparsers.add_parser('user', help="display user info")

args = parser.parse_args()

if args.cmd == 'push':
    pusher_api.push(args.body, args.title)
elif args.cmd == 'list':
    if args.d:
        pusher_api.list_devices()
    else:
        pusher_api.pushes_list()
elif args.user:
    pusher_api.user_info()