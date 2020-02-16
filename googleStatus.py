## googleStatus.py
## Gather infos from Google API's and send them to main.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------

import os
import requests
import datetime
import json

from msgs import buildHours

g_api_key = str(os.getenv('GOOGLE_API_KEY'))

link = "https://maps.googleapis.com/maps/api/place/details/json?key=" + g_api_key + "&place_id="


def getData(google_id_place):
	req = requests.get(link + google_id_place)

	res = json.loads(req.text)

	date = datetime.datetime.today()
	date_tomorrow = datetime.datetime.today() +  + datetime.timedelta(days=1)

	today = date.weekday()
	today_str = date.strftime('%A')

	tomorrow = date_tomorrow.weekday()
	tomorrow_str = date_tomorrow.strftime('%A')

	# print(today)

	open_data = res['result']['opening_hours']

	open_status = open_data['open_now']

	open_status_str = "Ouvert actuellement" if open_status else "Fermé actuellement"

	open_hours_raw = open_data['weekday_text'][today][len(today_str)+2::]

	open_hours = "Fermé aujourd'hui." if open_hours_raw == "Closed" else open_hours_raw

	open_hours_tomorrow_raw = open_data['weekday_text'][tomorrow][len(tomorrow_str)+2::]

	open_hours_tomorrow = "Fermé demain." if open_hours_tomorrow_raw == "Closed" else open_hours_tomorrow_raw

	phone_number = res['result']['international_phone_number']

	return buildHours(open_status, open_status_str, open_hours, open_hours_tomorrow, phone_number)

