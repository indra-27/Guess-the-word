from food import food
from country import country
from sports import sports
from movies import movies
from character import character
from fighternames import fighternames
from appliances import appliances
from chemicals import chemicals
from cswords import cswords


def guessing(word):
    print('Guess the Character:')
    guesses = ' '
    turns=15
    points=100
    while(turns>0):
        failed=0
        for char in word:
            if char in guesses:
                print(char)
                
            else:
                print("_")
                failed+=1
        print("Your points = ",points)
        if(failed==0):
            print("YOU WON!!!")
            print("The word is ",word)
            print("Your earned points = ",points)
            break
            
        guess=input('Guess the character:')
        
        guesses+=guess
        points+=10
        if guess not in word:
            turns-=1
            points-=15
            print("Wrong")
            print("Your points = ",points)
            print("You have ",+turns,"more guesses")
            if turns==0:
                print("You LOSE")
                print("The word is ",word)
                print("Better Luck next time!")
                exit()
def level1():
    print('WELCOME TO LEVEL 1 !!!')
    print('You are provided with 100 points :)')
    print('Select your preferred topic: ')
    print(' 1.INDIAN CUISINE\n 2.SPORTS\n 3.HOLLYWOOD MOVIES\n')
    ch=(input('Enter your choice: '))
    if(ch=='1' ):
      word= food()
    elif(ch=='2' ):
      word = sports()
    elif(ch== '3'):
      word = movies()
    else:
      print('Invalid choice!')
      exit()
    guessing(word)

def level2():
    print('WELCOME TO LEVEL 2 !!!')
    print('Select your preferred topic: ')
    print(' 1.COUNTRY NAMES\n 2.CARTOON CHARACTERS\n 3.CHEMICAL ELEMENTS\n')
    ch=(input('Enter your choice: '))
    if(ch=='1' ):
      word = country()
    elif(ch=='2' ):
      word =character()
    elif(ch== '3'):
      word = chemicals()
    else:
      print('Invalid choice!')
      exit()
    guessing(word)


def level3():
    print('WELCOME TO LEVEL 3 !!!')
    print('Select your preferred topic: ')
    print(' 1.FREEDOM FIGHTERS\n 2.APPLIANCES\n 3.WORDS RELATED TO COMPUTERS\n')
    ch=(input('Enter your choice: '))
    if(ch=='1' ):
      word = fighternames()
    elif(ch=='2' ):
      word =appliances()
    elif(ch== '3'):
      word = cswords()
    else:
      print('Invalid choice!')
      exit()
    guessing(word)


print("\n\t\t\t\tGUESS THE WORD\t\t\t\n")
print("WELCOME TO THIS GAME!\nYou have to guess the given WORD\n")
print("Get an IDEA about this GAME :)\n")
print(" 1.This game has 3 levels.\n 2.LEVEL 1(Easy)\n   LEVEL 2(Medium)\n   LEVEL 3(Hard) ")
print(" 3.You are given with 100 points.\n 4.For every wrong guess you will lose 5 points and for every right guess you will gain 10 points.")
print(" 5.Once you complete a current level you will move to the next.\n")
print("NOTE: Don't use upper case letter")
name = input("Enter your Name : ")
print("Good Luck :) ", name)
level1()
level2()
level3()