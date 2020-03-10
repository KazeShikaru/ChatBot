from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

class SentimentAnalyzer(Component):

    #initializes variables and arrays
    name = "sentiment"
    provides = ["entities"]
    requires = []
    defaults = {}
    language_list = ["en"]

    #initializes the super class 
    def __init__(self, component_config=None):
        super(SentimentAnalyzer, self).__init__(component_config)

    #model is already trained unecessary
    def train(self, training_data, cfg, **kwargs):
        pass

    #converts the sentiment and confidence into a format compatible with the rasa format
    def convert_to_rasa(self, value, confidence):
        if (value == "neg"):
                  print("Sad bot")
	
        entity = {"value": value,
                  "confidence": confidence,
                  "entity": "sentiment",
                  "extractor": "sentiment_extractor"}

        return entity

    #process message to retireve sentiment
    def process(self, message, **kwargs):
        #initializes sentiment intensity analyzer
        sid = SentimentIntensityAnalyzer()
        #tries to generate the intensite of the sentiment (low,medium,high)
        res = sid.polarity_scores(message.text)
        #return the highest sentiment in the message
        key, value = max(res.items(), key=lambda x: x[1])
        #coverts the highest sentiment and how confident it is to rasa style
        entity = self.convert_to_rasa(key, value)
        #set the entities contained on the message
        #   name or subject contained on the message
        message.set("entities", [entity], add_to_output=True)

    #does nothing as model is already pre-trained
    def persist(self, model_dir,yam):
        pass