#!/bin/env python3
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import time

re='\033[1;31m'
gr='\033[1;32m'
cy='\033[1;36m'

def add(client):
    input_file = sys.argv[1]
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=',', lineterminator='\n')
        next(rows, None)
        for row in rows:
            user = {}
            user['id'] = int(row[0])
            user['username'] = row[1]
            user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.append(user)

    chats = []
    last_date = None
    chunk_size = 200
    groups=[]

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash = 0
    ))

    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue

    for index, group in enumerate(groups):
        print(f'{re}{str(index)} {cy}- {group.title}')

    g_index = input(f'{gr}[+] Enter Group Number To Add Members :{re}')
    target_group = groups[int(g_index)]
    target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

    print(f'{re}[1] Add by User ID\n[2] Add by Username')
    mode = int(input(f'{gr}Input :{re}')) 
    n = 0

    for user in users:
        n += 1
        if n % 50 == 0:
            try:
                print('Adding {}'.format(user['id']))
                if mode == 2:
                    if user['username'] == '':
                        continue
                    user_to_add = client.get_input_entity(user['username'])
                elif mode == 1:
                    user_to_add = InputPeerUser(user['id'], user['access_hash'])
                else:
                    client.disconnect()
                    sys.exit(f'{re}[!] Invalid Mode Selected. Exiting')
                client(InviteToChannelRequest(target_group_entity, [user_to_add]))
                print(f'{gr}[+] Waiting for 7 Seconds')
                time.sleep(7)
            except PeerFloodError:
                client.disconnect()
                sys.exit(f'{re}[!] Getting Flood Error from TeleGram. \n[!] Script is stopping now. \n[!] Please try again after some time.')
            except UserPrivacyRestrictedError:
                print(f'{re}[!] The user\'s settings do not allow adding. Skipping user.')
            except:
                print(f'{re}[!] Unexpected Error')
                continue
    client.disconnect()
    sys.exit(f'{gr}[+] {str(n)} Members successfully added to {group.title}.')

