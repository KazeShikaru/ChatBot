import socket
import requests
import json
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 28858))

sock.listen()

connection, address = sock.accept()

while True:

	message = connection.recv(1024)

	if message:
		print('Message Received: ' + message)
		payload = {'message': message, 'sender':"username"}
		payload = json.dumps(payload)
		r = requests.post('http://localhost:5005/webhooks/rest/webhook', payload)
		start = r.text.find('text":"')+7
		end = r.text.find('"}]')
		print('Our message: ' + r.text[start:end])
		connection.sendall(r.text[start : end ])
		if input == "stop":
			break;

connection.close()