'''
Favourite Number

Version: 0.1
Author: Yizhe
'''
import json
filename = 'favourite_numbers_10-11.json'
def test():
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        get_number()
    else:
        read_and_print_number()

def get_number():
    get_fav_number = input("Please input your favourite number: ")
    with open(filename, 'a') as f_obj:
        json.dump(get_fav_number, f_obj)

def read_and_print_number():
    with open(filename, 'r') as f_obj:
        fav_number = json.load(f_obj)
        print("I know your favourite number! It's " + fav_number + "!")

test()