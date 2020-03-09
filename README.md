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
#delete
#Dependencies: Spacy, Rasa, Tensorflow 2.0, Nvidia Cuda,
#installation guide for Rasa: https://rasa.com/docs/rasa/user-guide/installation/

First, you will need to install Rasa:https://rasa.com/docs/rasa/user-guide/installation/.
Afterwards install Anaconda for python 3.7
After installing and launching anaconda. Inside it import the virtual environment file (environment.yml) contained inside the project folder (ChatBot -> rasa). It may take a while to import it due to the high number of Dependencies.
Afterwards, In


File Organization:



Current Pipeline:
-SpacyNLP
-SpacyTokenizer
-SentimentAnalyzer
-SpacyFeaturizer
-RegexFeaturizer
-CRFEntityExtractor

Known Issues:
