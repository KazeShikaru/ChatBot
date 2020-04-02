import socket
import requests
import json
import sys

while True:

	if message:
		payload = {'message': message, 'sender':"username"}
		payload = json.dumps(payload)
		r = requests.post('http://localhost:5005/webhooks/rest/webhook', payload)
		start = r.text.find('text":"')+7
		end = r.text.find('"}]')
		if input == "/stop":
			break;