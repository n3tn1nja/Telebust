# Telebust
### Telegram Mass Group Adder, Group Scraper and Mass User Messaging.
#### Features
* Download all the members from a telegram group into a CSV file.
* Send message to every member in your saved CSV file. 
* Add all the members in your CSV file to a specified group. 


## Setup
### Download Repository
* `$ git clone https://github.com/n3tn1nja/telebust.git`
* `$ cd telebust`

### Create API Credentials 
* Go to https://my.telegram.org
* Go to API / Developer Section
* Create Telegram App

### Configure App
#### Install App Requirements & Setup Configration ( API ID, API Hash )
* `$ python3 bot.py -s` or `$ python3 bot.py --setup`

## Commands
### Scrape Group Users
* `$ python3 bot.py -sc` or `$ python3 bot.py --scrape`

### Add Members To Group
* `$ python3 bot.py -a members.csv` or `$ python3 bot.py --add members.csv`

### Send Message to Members
* `$ python3 bot.py -m members.csv` or `$ python3 bot.py --message members.csv`
