## main.py
## Gather infos from API's and send them to Slack via a Bot.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------

import os
import requests
import random

import grandPere
import hibiki
import kebab
import msgs
import pipio

import ptitCafe
import houblo

from dotenv import load_dotenv
load_dotenv()

# To Get Google Place ID :
# Go to : https://developers.google.com/places/web-service/place-id

slackURL = "https://hooks.slack.com/services/" + os.getenv('SLACK_URL_TOKEN')

## Functions Send
def sendMsg(msg):
    dataPOST = {'text': msg}
    req = requests.post(slackURL, json=dataPOST)
    # print(req.status_code)

def sendAttachment(msg):
    dataPOST = {'attachments': msg}
    req = requests.post(slackURL, json=dataPOST)
    # print(req.status_code)

## Menus

print("Getting Menu from : P'tit Cafe")
ptitCafeMenu = ptitCafe.getLastMenu()

print("Getting Menu from : La Houblonnière")
houbloMenu = houblo.getLastMenu()

print("Getting Menu from : Grand Pere")
grandPereMenu = grandPere.getLastMenu()

print("Getting Menu from : Chez Victor")
kebabMenu = kebab.getLastMenu()

print("Getting Menu from : Chez Pipio")
pipioMenu = pipio.getLastMenu()

print("Getting Menu from : Japonais HiBiKi")
hibikiMenu = hibiki.getLastMenu()

## SEND EVERYTHING !

print("Sending...")

# Welcome
sendMsg(random.choice(msgs.welcomeTitle) + "\n" + random.choice(msgs.welcomeMsg))

# Menus
sendAttachment(ptitCafeMenu)
sendAttachment(houbloMenu)
sendAttachment(grandPereMenu)
sendAttachment(kebabMenu)
sendAttachment(pipioMenu)
sendAttachment(hibikiMenu)

print("Sent.")
