import json
filename = 'usernames.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome home, " + username + "!")