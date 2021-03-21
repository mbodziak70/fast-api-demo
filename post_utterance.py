# -*- coding: utf-8 -*-

import requests

#*********************************************************************
#* MAIN
#*********************************************************************

message = {'text': 'Niespodzianka, czyż nie?'}

url = 'http://127.0.0.1:80/alium-at/process_utterance/'
url = 'http://35.234.117.20:80/alium-at/process_utterance/'
r = requests.post(url, json=message)
print(r.json())
