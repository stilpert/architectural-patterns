import urllib.request
import json


def get_message():
    url = 'http://localhost:3000/get_message'
    response = urllib.request.urlopen(url)
    return response.read().decode()


def post_message(new_sound):
    url = 'http://localhost:3000/set_message'
    data = {'sound': new_sound}
    data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers={
                                 'Content-Type': 'application/json'})
    response = urllib.request.urlopen(req)
    return response


if __name__ == '__main__':
    while True:
        new_sound = input('New message or enter: ').strip()
        if new_sound:
            post_message(new_sound)
        print('Curr sound:', get_message())
