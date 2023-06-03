#!/bin/env python3
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv, sys

re='\033[1;31m'
gr='\033[1;32m'
cy='\033[1;36m'

def scrape(client):
    chats = []
    groups = []

    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=500,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue

    print(f'{gr}[+] Choose a group to scrape members :{re}')

    for i, group in enumerate(groups):
        print(f'{re}{str(i)}{cy} - {group.title}')

    g_index = input(f'{gr}[+] Enter Group Number :{re}')
    target_group = groups[int(g_index)]

    all_participants = []
    all_participants = client.get_participants(target_group, aggressive=True)

    print(f'{gr}[+] Saving Members In File...')

    with open(f'members-{target_group.title}-{str(target_group.id)}.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['user_id', 'username', 'access_hash', 'name'])

        for user in all_participants:
            if user.username:
                username = user.username
            else:
                username = ''
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ''
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ''
            name = (first_name + ' ' + last_name).strip()
            writer.writerow([user.id, username, user.access_hash, name])      

    client.disconnect()
    sys.exit(f'[+] {str(len(all_participants))} Members scraped successfully.')