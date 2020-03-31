from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

import nltk

import os

class NamedEntityRecognizer(Component):

    #initializes the super class contructor
    def __init__(self, component_config=None):
        super(NamedEntityRecognizer, self).__init__(component_config)

    #model is already trained unecessary
    def train(self, training_data, cfg, **kwargs):
        pass



    #process message to retireve sentiment
    def process(self, message, **kwargs):
       tokens = nltk.word_tokenize(message.text)
       tagged = nltk.pos_tag(tokens)
       entities = nltk.chunk.ne_chunk(tagged)
       print(str(entities))


    #does nothing as model is already pre-trained
    def persist(self, model_dir,yam):
        pass