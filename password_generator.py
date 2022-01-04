#Josh Follmer, password generator assignment

from random import randint


def make_password():
    '''
    Function that will ask you between a smaller and larger file containing random words, and will pick 4 words at random, 4 times, to make 4 possible passwords
    '''
    #its in a try loop in case  of errors when opening the file
    
    choice = input("Large file or small file?\n")
    #if the user wants the big file
    if choice in ['large file', 'large', 'l']:
        try:
            #opens the big file in read mode
            word_file = open('words_alpha.txt', 'r')
        #the only thing that could go wrong is the file not being found, so its unneccesary to be specific with the exception
        except:
            #gives instructions and ends the program
            print("File couldn't be found, please move words_alpha.txt into the same folder as password_generator.py.")
            exit()
        #sets a variable to be all the lines in it
        lines = word_file.readlines()
        #makes 4 passwords
        for i in range(4):
            #makes 4 variables to 4 random lines, and strips the excess spaces
            word0 = lines[randint(0, 370100)].strip()
            word1 = lines[randint(0, 370100)].strip()
            word2 = lines[randint(0, 370100)].strip()
            word3 = lines[randint(0, 370100)].strip()
            #if any of those choices are less than 6 letters, it will loop until it picks one that isnt for each word
            while len(word0) < 6:
                word0 = lines[randint(0, 370100)].strip()
            while len(word1) < 6:
                word1 = lines[randint(0, 370100)].strip()
            while len(word2) < 6:
                word2 = lines[randint(0, 370100)].strip()
            while len(word3) < 6:
                word3 = lines[randint(0, 370100)].strip()
            #makes a password variable with the 4 words with a space between them
            password = word0 + ' ' + word1 + ' ' + word2 + ' ' + word3
            #prints it out 4 times
            print(f"Password {i}: {password}")
            word_file.close()
    #if the user wats the smaller file
    elif choice in ['small file', 'small', 's']:
        #this is all the same process but for the smaller file
        try:
            word_file = open('10000_words.txt', 'r')
        except:
            print("File couldn't be found, please move 10000_words.txt into the same folder as password_generator.py.")
            exit()
        
        lines = word_file.readlines()
        for i in range(4):
            word0 = lines[randint(0, 10000)].strip()
            word1 = lines[randint(0, 10000)].strip()
            word2 = lines[randint(0, 10000)].strip()
            word3 = lines[randint(0, 10000)].strip()
            while len(word0) < 6:
                word0 = lines[randint(0, 10000)].strip()
            while len(word1) < 6:
                word1 = lines[randint(0, 10000)].strip()
            while len(word2) < 6:
                word2 = lines[randint(0, 10000)].strip()
            while len(word3) < 6:
                word3 = lines[randint(0, 10000)].strip()
            password = word0 + ' ' + word1 + ' ' + word2 + ' ' + word3
            print(f"Password{i}: {password}")
            word_file.close()

    else:
        #this is so the user wont break the program by entering something wrong
        print("You need to enter large file, large, l, or small file, small, or s")
        make_password()
    #will close the file always, even if it wasnt opened
    
    


make_password()
