def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename) as f_ojb:
            contents = f_ojb.read()
    except FileNotFoundError:
        pass
        print('nothing found')
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)