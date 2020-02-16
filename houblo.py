## houblo.py
## Gather infos from Facebook API's and send them to main.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------

import os
import requests
from datetime import datetime
import msgs

from facebook_scraper import get_posts

from googleStatus import getData

now = datetime.now()

## Consts :
title = "La Houblonnière"
link = "https://www.facebook.com/BIERSTUBLAHOUBLONNIERE"
page_id = "BIERSTUBLAHOUBLONNIERE"

google_id_place = "ChIJQftOLm_IlkcRM2Ksn9LGJDA"


def getLastMenu():
	googleData = getData(google_id_place)

	if googleData['boolean']:
		return getMenu(googleData['status'], googleData['phone_number'])
	else:
		return msgs.buildClosed((title + " (" + googleData['status'] + ")"), link, (googleData['hours'] + "\nDemain : " + googleData['tomorrow']))


def getMenu(status_open, phone_number):
	articles = get_posts(page_id, pages=2)

	for article in articles:
		# print(article['text'].splitlines())
		return msgs.buildMenu((title + " (dernier post) (" + status_open + ")"), link, article['text'].splitlines()[0],
							  article['post_url'], (article['text'].splitlines()[1::] + "\nTéléphone : " + phone_number))