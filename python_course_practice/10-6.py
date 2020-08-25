'''
Addition

Version: 0.1
Author: Yizhe
'''
while True:
    try:
        b = input('Plz input the numbers: ')
        if b == 'q':
            break
        b = int(b)
        
        a = input("Give me another number: ")
        if a == 'q':
            break
        a = int(a)
    except ValueError:
        pass
        print("That was not a number.")

    else:
        total = a + b
        print('The result of the two numbers is ' + str(total) + '.')