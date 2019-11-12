## main.py
## Gather infos from API's and send them to Slack via a Bot.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------

import os
from dotenv import load_dotenv
import requests
import json
import random
import msgs

import ptitCafe

load_dotenv();

## Functions Send
def sendMsg(msg):
    slackURL = "https://hooks.slack.com/services/" + os.getenv("SLACKURLTOKEN");
    dataPOST = {'text': msg}
    req = requests.post(slackURL, json=dataPOST);

def sendAttachment(msg):
    slackURL = "https://hooks.slack.com/services/" + os.getenv("SLACKURLTOKEN")
    dataPOST = {'attachments': msg}
    req = requests.post(slackURL, json=dataPOST)

## Menus

# Get Ptit Cafe
print("Getting Menu from : Petit Cafe")
ptitCafeMenu = ptitCafe.getLastMenu()

## SEND EVERYTHING !

print("Sending...")

# Welcome
sendMsg(random.choice(msgs.welcomeTitle) + "\n" + random.choice(msgs.welcomeMsg))

# PtitCafe
sendAttachment(ptitCafeMenu)

print("Sent.")
