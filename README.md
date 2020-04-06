# ChatBot
Project for COSC 310 Software Engineering

This is an interactive conversational agent that responds to user input, also known as a chat bot. It is created using the Rasa framework for AI assistants. It uses data sets we have written that contain lists of potential conversation topics that the user may ask about called intents as well as "stories" which represent conversation structures, and a domain of responses that the chat bot may use in its responses. The bot will try to decide which story to use, and act according to that conversation structure.

## Team Members:<br>
  Carter Phillips<br>
  Ren Lin<br>
  Rickson Reichmann<br>
  Will McFarland<br>

## Language and Tools used:
Main language: Python 3<br>
Framework: [rasa](https://rasa.com/)

## Project Structure and Organization

**data/nlu.md:** Contains intents, which are topics that the user might ask about

**data/stories.md:** Contains common structuers or flows of conversations. This is how the bot knows how to respond to user input. The user's input gets classified as an intent, and then the stories tell the bot what to do in response to a given intent.

**domain.yml:** A central file that links together all actions, intents, and entities defined in nlu and stories files. It also contains all specific responses or "utter"-ings for the bot. That is, the story specifies which response in the domain to use.

## Current Pipeline:
The pipeline consists of multiple pieces of codes designed to transform data from one step to the next in order to achieve an overall goal.
Currently our pipeline is composed of these following components:
-SpacyNLP<br>
-SpacyTokenizer<br>
-SentimentAnalyzer<br>
-SpacyFeaturizer<br>
-RegexFeaturizer<br>
-CRFEntityExtractor<br>


## Installation and running guide (current version)

First, install Anaconda for python 3.7. After installing it and launching anaconda. Inside it import the virtual environment file `environment.yml` contained inside the project folder `./rasa`. It may take a while to import it due to the high number of Dependencies.
Now, use pip to install 'nltk', then using python import ntlk and download vader_lexicon `nltk.download('vader_lexicon')`.<br><br>
Then, you will need to install Rasa and its dependencies (Spacy): https://rasa.com/docs/rasa/user-guide/installation/. You may need to install it inside the rasa terminal. Look at the following instruction on how to do it. <br><br>
Afterwards, Inside Anaconda on the environments tab click the arrow on top of the environment named `rasa`. This will load the environment. After it is loaded click the arrow again and select the option run in terminal. This will create a new command prompt. <br>
Inside it change the directory to the folder where your project is located. There, use the command (rasa shell).<br>

If you get the following exception ` rasa.nlu.model.UnsupportedModelError: The model version is too old to be loaded by this Rasa NLU instance.`. You may need to re-train the data before starting it. So, run `rasa train`. This may take a while to complete.<br>

When done you can run the command `rasa shell` to start the command prompt version of the bot. If it does not work you may need to delete all models inside the `.\rasa\models`. And re-train it again.
<br><br>
If you want to manually run the GUI version. First you need to install pyspellchecker on rasa enviroment and on the your computer `pip install pyspellchecker`.After that use the following command: `rasa run -m models --enable-api --cors "*" --debug` to start the server. After that run the file `gui.py` to start the gui.
<br><br>
You can also run the UI and Server together by running the file `mainRun.py` from inside the rasa enviroment terminal. However, if you try to send a message in the gui before it connects to the server the GUI will error out.


## Features that can be converted to APIs
  GUI<br>
  Spelling Corrector<br>
  Socket Communication<br>
  Flower Decider<br>
  Suggest Music<br>
  Bot connector<br>

## Features Implemented (since last version)
Functions added include a modified flower and potato recommendation system, a custom gui, a flower recommendation system, more training, sentiment analysis, entity recognition, and spelling checker on the gui.<br>
Training data now contains spelling errors to account for user spelling mistakes. Altought, the system should be sufficiently capable of ignoring most spelling errors on low value words anyway.


