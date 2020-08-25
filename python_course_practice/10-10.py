'''
Common Words

Version: 0.1
Author: Yizhe
'''
def count_words(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        print("The word 'the' appears in the " + str(filename) + " about " + str(contents.lower().count('the')) + " times.")
count_words('little_women.txt')