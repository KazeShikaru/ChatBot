import os
import time
import importlib
import gui as gui

#importlib.import_module('gui')

os.system('pip install pyspellchecker')
os.system('cls')
print('please wait while the system launches')
os.system('start cmd /k "rasa run -m models --enable-api --cors "*" --debug"')
os.system('start cmd /k "rasa run actions"')
time.sleep(5)
ready = False
while (not ready) :
	try:
		gui.run()
		ready = True
		pass
	except Exception as e:
		time.sleep(1)

exit(0)
