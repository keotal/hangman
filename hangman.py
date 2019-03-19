from random import *

# word list
wordlist = ['red', 'blue', 'green', 'yellow']

# choose random word from word list
gameword = list(wordlist[randint(0, 3)])

print(gameword)


guesses = list(len(gameword) * "_")

def game() :
    tries = 5
    
    #game loops until you get 5 incorrect answers
    while tries > 0 :

        #accepts user input
        guess = input("")
        
        #if the letter is in the gameword, replace '_' with the letter
        #if not, reduce the number of tries 
        if guess in gameword and len(guess) == 1:
            for i in range(len(gameword)): 
                if guess == gameword[i]:
                    print("You got a hit!")
                    guesses[i] = guess
        else:
            print("No " + guess + "'s")
            tries -= 1
            print("You have " + str(tries) + " tries left!")
        
        print(guesses)

        #loop breaks if all guesses are correct
        if guesses == gameword:
            print("You Win!")
            break

        

# game loop
game()
print('Game Over!')
    