import json
import difflib
import sys

with open('data.json','r') as fh:
    dictionary = json.load(fh)

def lookup(w):
    try: 
        return dictionary[w.lower()]
    except KeyError:
        close = [entry for entry in dictionary.keys() if difflib.SequenceMatcher(None, entry, w).ratio() > .75]
        if close:
            return "Do you mean any of these words: " + ", ".join(close) + "?"
        else:
            return "Word not found"

while True:
    word = input("Enter word: ")

    if word == 'EXIT':
        sys.exit()

    print(lookup(word))

