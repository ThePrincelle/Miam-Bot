## msgs.py
## Preparing messages for Slack API.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------

import random

## Const Messages
welcomeTitle = [
	"Bonjour !",
	"Hello !",
	"Aloha !",
	"Hey ;)"
]

welcomeMsg = [
	"Voici les menus du jour :",
	"Voilà ce qu'il y a pour aujourd'hui :",
	"Voyons ce qu'il y a de bon pour aujourd'hui :",
	"Vous avez faim ? Voilà ce qu'il y a :",
	"Maaaaanger !!! :"
]

nothingMsg = [
	"Désolé, mais aucun menu n'est disponible pour ce jour-ci...",
	"Navré. Je n'ai aucune information sur le menu du jour...",
	"Je ne trouve pas le menu du jour..."
]


## Building Messages


def buildHours(boolean, status, hours, tomorrow, phone_number):
	return {
		"boolean": boolean,
		"status": status,
		"hours": hours,
		"tomorrow": tomorrow,
		"phone_number": phone_number
	}


def buildClosed(title, linkWebsite, hours):
	return [{
		"author_name": title,
		"author_link": linkWebsite,
		"text": hours
	}]


def buildMenu(title, linkWebsite, menuTitle, menuLink, menuContent):
	return [{
		"author_name": title,
		"author_link": linkWebsite,
		"title": menuTitle,
		"title_link": menuLink,
		"text": menuContent
	}]


def noMenu(title, linkWebsite, text):
	return [{
		"author_name": title,
		"author_link": linkWebsite,
		"text": random.choice(nothingMsg) + "\n" + text
	}]
