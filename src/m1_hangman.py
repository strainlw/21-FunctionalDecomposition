"""
Hangman.

Authors: Loki Strain and Ezrie McCurry.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import random


def main():
    game()



def word(minlength):

    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()

    while True:
        item = words[random.randrange(0,len(words))]
        if len(item) >= minlength:
            return item

def guess(gword, list,guesses,count):

    print('Guesses left: ', guesses - count)

    g = input('What do you guess?')

    for k in range(len(gword)):
        if g == gword[k]:
           pword(k, list, g)


    for k in range(len(list)):
        print(list[k],end='')
    print()






def pword(k, list, g):
    list[k] = g

def win(list,gword):
    returning = True
    for k in range(len(gword)):
        if list[k] != gword[k]:
            returning = False
    return returning

def game():

    while True:
        play = input('Do you want to play?')
        if play == 'yes':
            print("Lets hang some men!!")

            minlength = int(input('What is the smallest number of letters?'))

            guesses = int(input('How many guesses do you want?'))

            gword = word(minlength)


            list1 = makelist(gword)
            print_before(list1)
            gamestate(guesses,gword,list1)


        if play == 'no':
            break

def makelist(gword):
    list1 = []
    for k in range(len(gword)):
        list1 = list1 + ['-']
    return list1

def gamestate(guesses, gword, list1):
    count = 0

    for k in range(guesses):
        guess(gword, list1, guesses, count)
        count = count + 1
        if win(list1, gword) is True:
            print('You win!')
            return

        if count == guesses:
            print('It over you lose. The word was {}.'.format(gword))
            return


def print_before(list1):
    for k in range(len(list1)):
        print(list1[k], end='')
    print()
main()

