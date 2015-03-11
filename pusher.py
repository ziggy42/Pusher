#!/usr/bin/env python3
import argparse
import json
import requests
import mimetypes

PUSH_URL = "https://api.pushbullet.com/v2/pushes"
DEVICES_URL = "https://api.pushbullet.com/v2/devices"
USER_URL = "https://api.pushbullet.com/v2/users/me"
UPLOAD_REQUEST_URL = "https://api.pushbullet.com/v2/upload-request"


def push(AccessToken, msg, title=None, device=None):
    print("Pushing '{0}'...\n".format(msg))
    
    data = { 
        'type' : 'note', 
        'title' : title, 
        'body' : msg, 
        'device_iden' : device
    }

    resp = requests.post(PUSH_URL, data=data, auth=(AccessToken, '')).json()
    if resp.get('error') == None:
        print("Push sent successfully")
    else:
        print("Error: {0}".format(resp.get('error')['message']))


def push_verbose(AccessToken, device=None):
    title = input("Push title: ")
    content = input("Push conentent: ")

    push(AccessToken, content, title, device)


def push_file(AccessToken, file_name):
    f = open(file_name, 'rb')
    file_type = mimetypes.guess_type(file_name)[0]

    print("Uploading {0}...".format(file_name))
    try:
        data = {
            'file_name': file_name, 
            'file_type' : file_type
        }

        headers = {'Authorization': 'Bearer ' + AccessToken, 'Content-Type': 'application/json'}
        resp = requests.post(UPLOAD_REQUEST_URL, data=json.dumps({'file_name': 'image.jpg'}), headers=headers).json()
        if resp.get('error') != None:
            print("Error: {0}".format(resp.get('error')['message']))
            return

        file_url = resp.get('file_url')
        resp = requests.post(resp.get('upload_url'), data=resp.get('data'), files={'file': f})

        data = { 
            'type' : 'file', 
            'file_name' : file_name, 
            'file_type' : file_type, 
            'file_url' : file_url, 
            'body' : ''
        }
        resp = requests.post(PUSH_URL, data=data, auth=(AccessToken, '')).json()
		

    except requests.exceptions.ConnectionError:
        print("Try again later.")
    f.close()


def get_device_list(AccessToken):
    print("Getting the devices that can be pushed to...\n")

    resp = requests.get(DEVICES_URL, auth=(AccessToken, '')).json()
    if resp.get('error') == None:
        for device in resp['devices']:
            if device['pushable']:
                print("ID: {0}\tDevice: {1}".format(device['iden'], device['nickname']))
    else:
        print("Error: {0}".format(resp.get('error')['message']))


def get_user_info(AccessToken):
    print("Getting user info...\n")

    resp = requests.get(USER_URL, auth=(AccessToken, '')).json()
    if resp.get('error') == None:
        print(("Iden: {0}\n"
            "Email: {1}\n"
            "Email Normalized: {2}\n"
            "Created: {3}\n"
            "Modified: {4}\n"
            "Profile Pic: {5}\n"
            "Name: {6}").format(resp['iden'], resp['email'], resp['email_normalized'], 
                resp['created'], resp['modified'], resp['image_url'], resp['name']))
    else:
        print("Error: {0}".format(resp.get('error')['message']))


def get_pushes_list(AccessToken):
    print("Getting pushes history...\n")

    resp = requests.get(PUSH_URL, auth=(AccessToken, '')).json()
    pushes = resp.get('pushes')

    for push in pushes:
        print(str(push) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pusher is a PushBullet command line client')
    parser.add_argument(dest='AccessToken')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-sp', help='Simple Push', metavar='MSG')
    group.add_argument('-spd', help='Simple Push to a selected device', metavar=('MSG', 'DEVICE_ID'), nargs=2)
    group.add_argument('-p', help='Push', action='store_true')
    group.add_argument('-pf', help="Push file",  metavar='FILE_NAME')
    group.add_argument('-pd', help='Push to a selected device', metavar='DEVICE_ID')
    group.add_argument('-i', help="Get user info",  action='store_true')
    group.add_argument('-l', help="Get device list",  action='store_true')
    group.add_argument('-pl', help="Get pushes history",  action='store_true')
    args = parser.parse_args()

    if args.sp != None:
        push(args.AccessToken, args.sp)
    elif args.spd != None:
        push(args.AccessToken, args.spd[0], '', args.spd[1])
    elif args.p:
        total_push(args.AccessToken)
    elif args.pd:
        push_verbose(args.AccessToken, args.pd)
    elif args.i:
        get_user_info(args.AccessToken)
    elif args.l:
        get_device_list(args.AccessToken)
    elif args.pf != None:
        push_file(args.AccessToken, args.pf)
    elif args.pl:
        get_pushes_list(args.AccessToken)
    else:
        total_push(args.AccessToken)