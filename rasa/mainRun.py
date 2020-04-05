import os
import time
from gui.py import run

os.system('pip install pyspellchecker')
os.system('cls')
os.system('start cmd /k "rasa run -m models --enable-api --cors "*" --debug"')
os.system('start cmd /k "rasa run actions"')
print('waiting for rasa to launch')
time.sleep(10)
ready = False
while (not ready) :
	try:
		print("AAAAAAAAAAAAAAAAAA")
		gui.run()
		ready = True
		pass
	except Exception as e:
		print(e)
		time.sleep(10)

exit(0)
