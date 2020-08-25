'''
Cats and Dogs

Version: 0.1
Author: Yizhe
'''
'''
def make_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)

make_file('cats.txt', 'cat1\ncat2\ncat3\n')
make_file('dogs.txt', 'dog1\ndog2\ndog3\n')
'''
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass
        # print('The file ' + filename + ' did not found.')

read_file('cats.txt')
read_file('dogs.txt')