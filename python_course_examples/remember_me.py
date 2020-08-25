import json

# Load the username, if it has been stored previously.
#  Otherwise, prompt for the username and store it.

def get_stored_names():
    """Get Stored username if avaliable."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input('Please input your name: ')
    filename = 'username.json'
    print("We'll remember you when you comeback, " + username + "!")
    with open(filename, 'a') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the users by name."""
    username = get_stored_names()
    if username:
        test = input("Are you " + username + "?(y/n)")
        if test == 'y':
            print("Welcom home, " + username + "!")
        else:
            get_new_username()
    else:
        get_new_username()

get_stored_names()
greet_user()