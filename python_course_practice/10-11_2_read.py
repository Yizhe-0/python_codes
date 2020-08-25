'''
Read and Print Favourite Nmuber

Version: 0.1
Author: Yizhe
'''
import json
filename = 'favourite_numbers_10-11.json'

def read_and_print_number():
    with open(filename, 'r') as f_obj:
        fav_number = json.load(f_obj)
        print("I know your favourite number! It's " + fav_number + "!")
read_and_print_number()