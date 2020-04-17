import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(user_input):
    user_input = user_input.lower()
    if user_input in data:
        return data[user_input]
    elif user_input.title() in data:
        return data[user_input.title()]
    elif user_input.upper() in data:
        return data[user_input.upper()]
    elif len(get_close_matches(user_input, data.keys())) > 0:
        close_match = get_close_matches(user_input, data.keys())[0]
        choice = input("Did you mean %s instead? Enter Y if yes, or N if no." % close_match)
        if choice == "Y":
            return data[close_match]
        elif choice == "N":
            return "The word doesn't exit! Please Enter a valid word!"
        else:
            return "We didn't understand you entry."
    else:
        return "The word doesn't exit! Please Enter a valid word!"


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



