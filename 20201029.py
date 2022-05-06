Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# sstudent ID - 20201029         Date -14/20/2021

import random,time
from time import sleep

while True:
        wordList = ["bus","car","go","banana","in","apple","game","lap","van",
                    "to","tree","wifi","sun","light","gun","to","phone","at","on","cup","hi"]
        name = input("Enter your name :")
        print("")
        print("Hello",name.capitalize(),"Get ready to play the game...")  #Capitalization of the name
        print("")
        print("_ GAME STARTED _")
        time.sleep(1)  #Printing is delayed for a while
        print("Let's Play Game..")
        time.sleep(0.5)  #Printing is delayed for a while
        guess = random.choice(wordList)  #Random selection of words
        print("Guess the word : ")
        print()
        letters = "-" * len(guess)   #Spacing the number of letters in the word
        print(letters)
        guessedList = []
        guessing = len(guess)  #Provide playing opportunities that match the number of letters in the word
        while guessing > 0:
            f = open("output.txt", "a")  #The history of our game is written in a TXT file
            word = input("Enter a letter:  ")
            exit_game = input("you can exit the game enter X or "
                              "enter any key you can continue the game : ")  #If the player wants to leave the game and continue playing
            if exit_game == "X":
                print("Thank you for playing the game..")
                break
            if len(word) > 1 or len(word) == 0:
                print("Please enter a single letter!")  #Enter only one letter at a time
            elif word.islower():
                pass
            else:
                print("no use the numbers.pleas enter the letter!")  #if user already guessed correct letter


            if word in guessedList:
                print("You already typed this letter,",guessing)  #Showing the number of times the thumbs have
                print("")
                print(letters)
                continue
            else:
                guessedList.append(word)
            if guessing == 0:
                print("Sorry, You lost !")  #Awareness of defeat
                print("")
                print("You are lost",guessing,file=f)  #Printing a TXT file about the defeat
                break
            if word in guess:       #Guess the correct word
                for j in range(len(guess)):
                    if guess[j] == word:
                        letters = letters[:j] + word + letters[j + 1:]   #Includes random letters in the selected word
                if letters == guess:
                    pass
                else:
                    print("")
                    print(letters)   #If the letter used is not in the word, it will be displayed
                if letters == guess:
                    print("woahh...you Won !! ")  #Notice of Winning
                    print("The correct word was ",guess)  #Exact word display
                    print("you Won",file=f)  #Printing a TXT file about the winnig
                    print("The player name was -", name, file=f)   #Printing a TXT file about the player name
                    print("The correct word was - ", guess, file=f)  #Printing a TXT file about the correct word
                    print("You used", len(guess), "chances", file=f)  #Printing a TXT file about the Number of instances used
                    print("")
                    break
            else:
                if len(word) > 1 or not word.islower():  #Number of instances used
                    print("The correct word is",word,file=f)
                    pass
                elif word in guessedList and word in guess:
                    pass
                else:
                    guessing -= 1
                    print("No such letter in the word ,please give appropriate word",guessedList)  #Notice that the letter used is not in the word
                    print("The wrong lettrs is",word, file=f)  #Printing a TXT file about the wrong letter
                    print("You have", guessing, "chance left")
                    print("")
                if guessing == 0:
                    pass
                else:
                    print("")
                    print(letters)
            if guessing == 0:
                print("Sorry, You lost!!")   #Notice of defeat
                print("The player name was -", name, file=f)  #Printing a TXT file about the player name
                print("The correct word was - ", guess, file=f)  #Printing a TXT file about the correct word
                print("You used",len(guess),"chances",file=f)  #Printing a TXT file about the Number of instances used
                print("You lost",file=f)  #Printing a TXT file about the defeat
                print("")
                break

        gameStart = input('Type "P" to play the game, "Q" to quit: ')  #Whether or not to play again
        print("----------------------------", file=f)
        f.close()

        if gameStart == "P" or gameStart=="p":  #If P is used, play again
            print("")
            continue
        elif gameStart == "Q" or gameStart=="q":   #If Q is used, quit the game
            print("Thank uu..")
            break
        else:
            print("Invalid input...")  #Notification that another letter was used
            print('Type "P" to play the game, "Q" to quit: ')
            break

