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
    #Recommends flowers
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


def suggestMusic():
    # Recommends music
    f = open("tempData/entities.txt", "r")
    lineRead = f.readlines()
    wordTally = {
        "angry": 0,
        "pain": 0,
        "hate": 0,
        "sad": 0,
        "melancholy": 0,
        "relax": 0,
        "energetic": 0,
        "beauty": 0,
        "lush": 0,
        "sombre": 0,
        "lonely": 0,
        "dark": 0,
        "happy": 0,
        "upbeat": 0,
        "downtempo": 0,
        "surreal": 0,
        "cold": 0,
        "soothing": 0,
        "calm": 0,
        "love": 0,
        "comfy": 0,
        "rainy": 0,
        "sunny": 0,
        "summer": 0,
        "chill": 0,
        "cloudy": 0,
        "heartbroken": 0,
        "bittersweet": 0,
        "vegan": 0,
        "space": 0,
        "snow": 0,
        "psychedelic": 0
    }
    for line in lineRead:
        for word in line.split():
            # word = str(word)
            if len(word) > 4:
                if word[-4:] == "/NNS":
                    if word[:len(word) - 5] in wordTally:
                        wordTally[word[:len(word) - 5]] = wordTally[word[:len(word) - 5]] + 1

                elif word[-3:] == "/NN":
                    if word[:len(word) - 3] in wordTally:
                        wordTally[word[:len(word) - 3]] = wordTally[word[:len(word) - 3]] + 1

    max = 0
    keyString = "angry"
    for k, v in wordTally.items():
        if v > max:
            max = v
            keyString = k

    switch = {
        "angry": "Death Grips",
        "pain": "Swans",
        "hate": "Death Grips",
        "sad": "Deaf Center, Florist, or Get Up by Xiu Xiu",
        "melancholy": "Florist or Max Richter's Blue Notebooks",
        "relax": "some cool jazz like Bill Evans or Dave Brubeck",
        "energetic": "Death Grips",
        "beauty": "Biosphere",
        "lush": "Because by Gary McFarland or Scott Walker",
        "sombre": "Mimicking Birds",
        "lonely": "911 / Mr. Lonely by Tyler, The Creator",
        "dark": "DJ Rashad for driving around the city at midnight or The Black Dog if you're sitting at your desk",
        "happy": "Kero Kero Bonito or Orchards",
        "upbeat": "Lizzy Mercier Descloux",
        "downtempo": "Zero 7",
        "surreal": "The Black Dog, Kelly Moran, or Biosphere",
        "cold": "Biosphere",
        "soothing": "some ambient music like Briano Eno or Steve Roach",
        "calm": "some ambient music like Briano Eno or Steve Roach",
        "love": "Weyes Blood or Angel Olsen",
        "comfy": "Sun Kil Moon or Joni Mitchell",
        "rainy": "Scott Walker or Into the Night by Julee Cruise",
        "sunny": "Lizzy Mercier Descloux or Orchards",
        "summer": "Lizzy Mercier Descloux, Allman Brothers, or LCD SoundSystem",
        "chill": "some of Aphex Twin's Ambient works",
        "cloudy": "The Breathing Effect or Will Ackerman",
        "heartbroken": "Bridge Over Troubled Water by Simon and Garfunkel or In the Air Tonight by Phil Collins",
        "bittersweet": "In the Aeroplane Over the Sea - Neutral Milk Hotel",
        "vegan": "Mort Garson",
        "space": "Harvey Sutherland or Steve Roach",
        "snow": "Snowline by Shadowfax",
        "psychedelic": "Guerilla Toss"

    }
    rec = "I recommend you listen to " + switch[keyString]
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


class ActionMusicRecommendation(Action):
    def name(self) -> Text:
        return "action_music_recommendation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=suggestMusic())
        return []
