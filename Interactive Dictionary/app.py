import json
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))

    # did you mean> (closest to input, compared with keys in data)

def meaning(w):
    suggestion = gcm(w.lower(),data.keys())
    if w.lower() in data:
        return data[w.lower()]
    elif len(suggestion) > 0:
        response = input(f"Did you mean {suggestion[0]}")
        if response.lower() == "yes":
            return data[suggestion[0]]
        else:
            return "Word Not Found."
    else:
        return "Nothing To Suggest."

result = meaning(input("Enter word to get meaning: "))

if type(result) == list:
    for i in result:
        print(i,"\n")
else:
    print(result)
