## ptitCafe.py
## Gather infos from 'le-ptit-cafe.fr' API's and send them to main.
## Created by Maxime Princelle (https://contact.princelle.org)
## ------

import requests
from datetime import datetime
import msgs

now = datetime.now()

## Consts :
ptitCafeTitle = "Petit Café"
ptitCafeLink = "http://le-ptit-cafe.fr"

def getRawJson():
    res = requests.get("http://le-ptit-cafe.fr/wp-json/wp/v2/posts?categories=4&per_page=1");
    return res.json();
    
def getLastMenu():
    json = getRawJson();

    dayNumber = now.strftime("%d")
    start = now.strftime("%Y-%m-")
    today = start + dayNumber;
    yesterday = start + str(int(dayNumber) - 1)

    cleanStuff = ["<p>", "</p>", "<b>", "</b>"]
    datePublish = json[0]['date'].split("T")[0]
    publish = json[0]['content']['rendered']
    publishTitle = json[0]['title']['rendered']
    
    if datePublish == today or datePublish == yesterday:
        for stuff in cleanStuff:
            publish = publish.replace(stuff, "");
        publish = publish.rstrip().replace("\n", "\n- ")
        return msgs.buildMenu(ptitCafeTitle, ptitCafeLink, ("Menu du " + publishTitle.lower() + " :"), json[0]['link'], ("- " + publish));

    return msgs.noMenu(ptitCafeTitle, ptitCafeLink);
