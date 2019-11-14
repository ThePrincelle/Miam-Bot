## houblo.py
## Gather infos from Facebook API's and send them to main.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------

import os
from dotenv import load_dotenv
import requests
from datetime import datetime
import msgs

load_dotenv()

now = datetime.now()

## Consts :
title = "La Houblonniere"
link = "https://www.facebook.com/pg/BIERSTUBLAHOUBLONNIERE/about/?ref=page_internal"

