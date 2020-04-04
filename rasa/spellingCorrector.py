from spellchecker import SpellChecker as check
import re

#receives a string as a parameter and fixes spelling errors
def process_str(s_aux):
    words = []

    #removes all punctuation and separate words into array
    for line in filter(None, re.split("[,.\n\r!?:\)(\"]+", s_aux)):
        for word in line.split(" "):
                if (len(word) > 0):
                    words.append(word)

    checker = check()
    aux = ""
    #change from word to fixed word
    for word in words:
        aux += checker.correction(word) + " "

    return aux
