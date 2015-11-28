import json
import os
import requests
import mimetypes


ACCESS_TOKEM_PAGE = "https://www.pushbullet.com/#settings/account"
PUSH_URL = "https://api.pushbullet.com/v2/pushes"
DEVICES_URL = "https://api.pushbullet.com/v2/devices"
USER_URL = "https://api.pushbullet.com/v2/users/me"
UPLOAD_REQUEST_URL = "https://api.pushbullet.com/v2/upload-request"


class API(object):


    def __init__(self, access_token=None):
        if access_token:
            self.token = access_token
        else:
            if os.path.isfile('auth.json'):
                with open('auth.json') as f:
                    token_json = json.load(f)
                    self.token = token_json['access_token']
            else:
                self.token = input("Insert your AccessToken (you can find it here: {0}): ".format(ACCESS_TOKEM_PAGE))  
                with open('auth.json', 'w+') as f:
                    json.dump(dict(access_token=self.token), f)


    def push(self, body='', title=''):
        data = { 
            'type' : 'note', 
            'title' : title, 
            'body' : body, 
        }

        resp = requests.post(PUSH_URL, data=data, auth=(self.token, '')).json()
        if resp.get('error'):
            print("Error: {0}".format(resp.get('error')['message']))


    def push_file(self, path, body=''):
        file_type = mimetypes.guess_type(path)[0]
        file_name = os.path.basename(path)

        data = {
            'file_name': file_name, 
            'file_type' : file_type
        }

        headers = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'} # Really?
        resp = requests.post(UPLOAD_REQUEST_URL, data=json.dumps({'file_name': 'image.jpg'}), headers=headers).json()
        
        if resp.get('error'):
            print("Error: {0}".format(resp.get('error')['message']))
            return

        file_url = resp.get('file_url')
        with open(path, 'rb') as f:
            resp = requests.post(resp.get('upload_url'), data=resp.get('data'), files={'file': f})

        data = { 
            'type' : 'file', 
            'file_name' : file_name, 
            'file_type' : file_type, 
            'file_url' : file_url, 
            'body' : body
        }

        resp = requests.post(PUSH_URL, data=data, auth=(self.token, '')).json()

        if resp.get('error'):
            print("Error: {0}".format(resp.get('error')['message']))

    
    def list_devices(self):
        resp = requests.get(DEVICES_URL, auth=(self.token, '')).json()
        if not resp.get('error'):
            for device in resp['devices']:
                if device['pushable']:
                    print("ID: {0}\tDevice: {1}".format(device['iden'], device['nickname']))
        else:
            print("Error: {0}".format(resp.get('error')['message']))


    def user_info(self):
        resp = requests.get(USER_URL, auth=(self.token, '')).json()
        if not resp.get('error'):
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


    def pushes_list(self, active_only=True):
        resp = requests.get(PUSH_URL, auth=(self.token, '')).json()
        pushes = resp.get('pushes')

        for push in pushes:
            if active_only:
                if push['active']:
                    print(str(push))
            else:
                print(str(push))


