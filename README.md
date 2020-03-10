# ChatBot
Project for COSC 310 Software Engineering

Participants:
Rick
Ren
Will
Carter

Planning:
Main language: Python 3

Project Expected Timespan:
3 lunar cycles.

Sponsor: Rick


Installation guide (current version)
First, you will need to install Rasa and its dependencies (Spacy):https://rasa.com/docs/rasa/user-guide/installation/.
Afterwards install Anaconda for python 3.7
After installing and launching anaconda. Inside it import the virtual environment file (environment.yml) contained inside the project folder (ChatBot -> rasa). It may take a while to import it due to the high number of Dependencies.
Afterwards, Inside Rasa on the environments tab click the arrow on top of the environment named "rasa". And select
the option run in terminal. This will create a new command prompt. Inside it move to the folder where your project is
located. There, use the command (rasa shell).

If you get the following exception( rasa.nlu.model.UnsupportedModelError: The model version is too old to be loaded by this Rasa NLU instance.). You may need to re-train the data before starting it. So, run (rasa train). This may take a while to complete.


File Organization:



Current Pipeline:
-SpacyNLP
-SpacyTokenizer
-SentimentAnalyzer
-SpacyFeaturizer
-RegexFeaturizer
-CRFEntityExtractor

Known Issues:
