# ChatBot
Project for COSC 310 Software Engineering

## Team Members:<br>
  Carter Phillips<br>
  Ren Lin<br>
  Rickson Reichmann<br>
  Just Will<br>

Sponsor: Rick

## Planning:
Main language: Python 3

## Project Expected Timespan:
3 lunar cycles.




## Installation guide (current version)

First, you will need to install Rasa and its dependencies (Spacy):https://rasa.com/docs/rasa/user-guide/installation/. <br>

Then, install Anaconda for python 3.7. After installing it and launching anaconda. Inside it import the virtual environment file `environment.yml` contained inside the project folder `./rasa`. It may take a while to import it due to the high number of Dependencies.
Now, using pythom import ntlk and download vader_lexicon `nltk.download('vader_lexicon')`.
Afterwards, Inside Rasa on the environments tab click the arrow on top of the environment named `rasa`. This will load the environment. After it is loaded click the arrow again and select the option run in terminal. This will create a new command prompt. Inside it change the directory to the folder where your project is located. There, use the command (rasa shell).<br>

If you get the following exception ` rasa.nlu.model.UnsupportedModelError: The model version is too old to be loaded by this Rasa NLU instance.`. You may need to re-train the data before starting it. So, run `rasa train`. This may take a while to complete.<br>

When done you can run the command `rasa shell` to start the command prompt version of the bot. If it does not work you may need to delete all models inside the `.\rasa\models`. And re-train it again.
<br>
If you want to run the prototype version of the GUI you the following command: `rasa run -m models --enable-api --cors "*" --debug` to start the server. After that open the file `index.html` inside `./rasa/Rasa_CustomUI-v_2.0-master/`.
Click the button on the bottom-right side of the window to open the chat window. And send a message to start loading the models. It may take a while to process. After it finishes loading the bot will be working.<br>

## Project Organization



## Current Pipeline:
-SpacyNLP<br>
-SpacyTokenizer<br>
-SentimentAnalyzer<br>
-SpacyFeaturizer<br>
-RegexFeaturizer<br>
-CRFEntityExtractor<br>

## Known Issues:
