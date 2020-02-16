## kebab.py
## Gather infos from Google API's and send them to main.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------
import msgs
from googleStatus import getData

title = "Japonais HiBiKi"
link = "https://g.page/restaurant-japonais-hibiki?share"

google_id_place = "ChIJI8nXjw7JlkcRHFuvGacjB2Q"


def getLastMenu():
	googleData = getData(google_id_place)

	if googleData['boolean']:
		return msgs.noMenu((title + " (" + googleData['status'] + ")"), link, ("Horaires : " + googleData['hours'] + "\nTéléphone : " + googleData['phone_number']))
	else:
		return msgs.buildClosed((title + " (" + googleData['status'] + ")"), link,
								(googleData['hours'] + "\nDemain : " + googleData['tomorrow']))
