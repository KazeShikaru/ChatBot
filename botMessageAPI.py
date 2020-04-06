import socket
import requests
import json
import sys

def botInput(message, sender):
	payload = {'message': message, 'sender':sender}
	payload = json.dumps(payload)
	r = requests.post('http://localhost:5005/webhooks/rest/webhook', payload)
	start = r.text.find('text":"')+7
	end = r.text.find('"}]')
	out = r.text[start:end]
	out = out.replace('"},{"recipient_id":"JOHN","text":"Did that help you?', '')
	return r.text[start:end]

def botInputCustomUrl(message, sender, url):
	payload = {'message': message, 'sender':sender}
	payload = json.dumps(payload)
	r = requests.post(url, payload)
	start = r.text.find('text":"')+7
	end = r.text.find('"}]')
	return r.text[start:end]