## grandPere.py
## Gather infos from Google API's and send them to main.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------
import msgs
from googleStatus import getData

title = "Au pain de mon Grand-Père"
link = "https://goo.gl/maps/aqbNbc9SR5eWT4Mx5"

google_id_place = "ChIJq2IzCW_IlkcRwVO7oaX5I64"


def getLastMenu():
	googleData = getData(google_id_place)

	if googleData['boolean']:
		return msgs.noMenu((title + " (" + googleData['status'] + ")"), link, ("Horaires : " + googleData['hours']))
	else:
		return msgs.buildClosed((title + " (" + googleData['status'] + ")"), link,
								(googleData['hours'] + "\nDemain : " + googleData['tomorrow']))
