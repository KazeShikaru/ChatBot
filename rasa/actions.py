# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import operator

def suggestFlower():
    f = open("tempData/entities.txt", "r")
    lineRead = f.readlines()
    wordTally = {
            "love":0,
            "marriage":0,
            "death":0,
            "loss":0,
            "pain":0,
            "hate":0,
            "hope":0,
            "sad":0,
            "pride":0,
            "inspiration":0,
            "glory":0,
            "beware":0,
            "truth":0,
            "humility":0,
            "indifference":0,
            "poverty":0,
            "foolishness":0
    }
    for line in lineRead:
        for word in line.split():
            #word = str(word)
            if len(word)>4:
                if word[-4:] == "/NNS":
                    if word[:len(word)-5] in wordTally:
                        wordTally[word[:len(word)-5]] = wordTally[word[:len(word)-5]]+1;

                elif word[-3:] == "/NN":
                    if word[:len(word)-3] in wordTally:
                        wordTally[word[:len(word)-3]] = wordTally[word[:len(word)-3]]+1;
            
    max = 0
    keyString = "love"
    for k, v in wordTally.items():
        if v> max:
            max = v
            keyString = k
    
    switch = {
            "love":"Gardenia",
            "marriage":"Myrtle",
            "death":"Cypress",
            "loss":"Ranunculus",
            "pain":"Marigold",
            "hate":"Aconite ",
            "hope":"Daisy",
            "sad":"Willow",
            "pride":"Amaryllis",
            "inspiration":"Angelica",
            "glory":"Bay tree",
            "beware":"Begonia",
            "truth":"Bittersweet",
            "humility":"Bluebell",
            "indifference":"Candytuft",
            "poverty":"Evergreen",
            "foolishness":"Columbine"
    }
    rec = "The flower I recommend is: "+switch[keyString]
    return rec

class ActionCalculate(Action):

    def name(self) -> Text:
        return "action_calculate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="2+2=4")
        return []

class ActionDecide(Action):

    def name(self) -> Text:
        return "action_decide"

    def run(self, dispatcher: CollectingDispatcher, 
	tracker: Tracker, 
	domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="I recommend russet potatoes")
        return []

class ActionFlowerRecommendation(Action):
    def name(self) -> Text:
        return "action_flower_recommendation"

    def run(self, dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
	domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text=suggestFlower())
        return []
