#!/bin/env python3
# Author: github.com/tristanh00
import os, sys, telegram_client
from modules import message, scraper, adder

re='\033[1;31m'
gr='\033[1;32m'
cy='\033[1;36m'

def banner():
	os.system('clear')
	print(f"""{re}  ______{cy}          __          {re}____{cy}                    __ 
{re} /_  __/{cy}  ___    / /  ___    {re}/ __ ){cy}  __  __   _____  / /_
{re}  / /{cy}    / _ \  / /  / _ \  {re}/ __  |{cy} / / / /  / ___/ / __/
{re} / /{cy}    /  __/ / /  /  __/ {re}/ /_/ /{cy} / /_/ /  (__  ) / /_  
{re}/_/{cy}     \___/ /_/   \___/ {re}/_____/{cy}  \__,_/  /____/  \__/
\nAuthor: tristanh00\nVersion: June 3, 2023\n""")

def main():
    banner()
    try:
        client = telegram_client.connect_telegram()
        if any ([sys.argv[1] == '--setup', sys.argv[1] == '-s']):
            telegram_client.setup()
        elif any ([sys.argv[1] == '--add', sys.argv[1] == '-a']):
            adder.add(client)
        elif any ([sys.argv[1] == '--scrape', sys.argv[1] == '-sc']):
            scraper.scrape(client)
        elif any ([sys.argv[1] == '--message', sys.argv[1] == '-m']):
            message.send(client)
        elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
            banner()
            print(f"""{cy}$ python3 bot.py
( --setup  / -s ) {gr}Setup & Install Requirements
{cy}( --add / -a ) {gr}Add Users from file to Group `python3 bot.py -a members.csv`
{cy}( --message / -m ) {gr}Send Message To Users `python3 bot.py -m members.csv`
{cy}( --scrape / -sc ) {gr}Scrape Users
""")
        else:
            banner()
            print(f'{re}[!] Unknown argument : {sys.argv[1]}')
            print(f'{gr}For help, use $ python3 bot.py -h or --help')
    except IndexError:
        banner()
        print(f'{re}[!] No argument')
        print(f'{gr}For help, use $ python3 bot.py -h or --help')

if __name__ == '__main__':
    main()