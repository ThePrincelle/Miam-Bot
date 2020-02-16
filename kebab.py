## kebab.py
## Gather infos from Google API's and send them to main.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------
import msgs
from googleStatus import getData

title = "Chez Victor - Kebab"
link = "https://goo.gl/maps/GGJmKPwy7gvEKwW67"

google_id_place = "ChIJQ_9JBvrJlkcRINzEq98I5fU"


def getLastMenu():
	googleData = getData(google_id_place)

	if googleData['boolean']:
		return msgs.noMenu((title + " (" + googleData['status'] + ")"), link, ("Horaires : " + googleData['hours']))
	else:
		return msgs.buildClosed((title + " (" + googleData['status'] + ")"), link,
								(googleData['hours'] + "\nDemain : " + googleData['tomorrow']))
