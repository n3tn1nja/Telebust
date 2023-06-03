#!/bin/env python3
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import csv, sys, time

re='\033[1;31m'
gr='\033[1;32m'
cy='\033[1;36m'

SLEEP_TIME = 30

def send(client):
    input_file = sys.argv[1]
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=',', lineterminator='\n')
        next(rows, None)
        for row in rows:
            user = {}
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.append(user)

    print(f'{gr}[1] Message via User ID\n[2] Send Message via Username')

    mode = int(input(f'{gr}Input :{re} '))
    message = input(f'{gr}[+] Enter Your Message : {re}')

    for user in users:
        if mode == 2:
            if user['username'] == '':
                continue
            receiver = client.get_input_entity(user['username'])
        elif mode == 1:
            receiver = InputPeerUser(user['id'], user['access_hash'])
        else:
            client.disconnect()
            sys.exit(f'{re}[!] Invalid Mode. Exiting.')

        try:
            print(f'{gr}[+] Sending Message to:', user['name'])
            client.send_message(receiver, message.format(user['name']))
            print(f'{gr}[+] Waiting {SLEEP_TIME} seconds')
            time.sleep(SLEEP_TIME)
        except PeerFloodError:
            client.disconnect()
            sys.exit(f'{re}[!] Spam/Flood Error from Telegram. \n[!] Messaging Stopped. \n[!] Please try again later')
        except Exception as e:
            print(f'{re}[!] Error:', e)
            print(f'{re}[!] Trying to continue...')
            continue
    client.disconnect()
    sys.exit(f'{gr}[+] Done. Message sent to all users.')
