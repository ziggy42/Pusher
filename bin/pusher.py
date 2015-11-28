#!/usr/bin/env python3
import argparse

from pusher import api


def setup_parser():
    parser = argparse.ArgumentParser(description='Pusher is a PushBullet command line client')
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True

    # Push
    parser_push = subparsers.add_parser('push', help='push command')
    parser_push.add_argument('body', help='the main content of the push')
    parser_push.add_argument('title', help='the title of the push', nargs='?')
    parser_push.add_argument('-f', metavar='path', help='file')

    # List
    parser_list = subparsers.add_parser('list', help="list command")
    parser_list.add_argument('-d', action='store_true', help="list devices")

    # User
    parser_list = subparsers.add_parser('user', help="display user info")
    return parser.parse_args()


pusher_api = api.API()
args = setup_parser()

if args.cmd == 'push':
    if args.f:
        pusher_api.push_file(args.f, args.body)
    else:
        pusher_api.push(args.body, args.title)
elif args.cmd == 'list':
    if args.d:
        pusher_api.list_devices()
    else:
        pusher_api.pushes_list()
elif args.cmd == 'user':
    pusher_api.user_info()