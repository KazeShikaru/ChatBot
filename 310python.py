import socket
import requests
import json
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('127.0.0.1', 12000))
print('we bound')
sock.listen()
print('we listening')

connection, address = sock.accept()
print("OOOEEE IT WORKED")

while True:

	message = connection.recv(1024).decode('utf-8')
	print('Message Received: ' + message)
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