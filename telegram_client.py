#!/bin/env python3
import configparser, sys, os
from telethon.sync import TelegramClient

re='\033[1;31m'
gr='\033[1;32m'
cy='\033[1;36m'

def setup():
	print(f'{gr}[+] Installing Requierments...')
	os.system("""
		pip3 install telethon configparser 
		python3 -m pip install telethon configparser
		touch api.data
	""")
	print(f'{gr} Requierments Installed.\n')

	print(f'{gr}[+] Setup Config File.\n')
	parser = configparser.RawConfigParser()
	parser.add_section('api')

	xid = input(f'{gr}[+] Enter API ID : {re}')
	parser.set('api', 'id', xid)

	xhash = input(f'{gr}[+] Enter Hash ID : {re}')
	parser.set('api', 'hash', xhash)

	xphone = input(f'{gr}[+] Phone Number (International Format) : {re}')
	parser.set('api', 'phone', xphone)

	file = open('api.data', 'w')
	parser.write(file)
	file.close()

	sys.exit(f'{gr}[+] Setup Complete!')

def connect_telegram():
    parser = configparser.RawConfigParser()
    parser.read('api.data')

    try:
        phone = parser['api']['phone']
        client = TelegramClient(phone, parser['api']['id'], parser['api']['hash'])
    except KeyError:
        sys.exit(f'{re}Run python3 bot.py --setup')

    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input(f'{gr}[+] Enter Auth Code :'))

    return client