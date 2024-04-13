import random
# Imports the randint command. This is what randomly selects the word for you. 

print("Welcome to Luka's Hangman! Ready to play?")
print("Choosing a random word...")

# List of possible words that can be used (Amount is 25)
randomword = "adult", "choke", "refer", "sniff", "crown", "point", "shame", "witch", "bride", "merit", "leave", "steak", "stamp", "gloom", "pilot", "harsh", "onion", "stain", "value", "snake", "venus", "sugar", "chaos", "humor", "steam"

# Chooses the word from the list above randomly.
word = randomword[random.randint(0, 24)]

# Asks user for what type of game they want; letter guessing or word guessing.
word_or_letter = input("Would you like to guess a word or letter? ")
if word_or_letter == "word":
   
   # Prompts the user for first word guess. If correct, they win. If incorrect, we start hanging the man. The code repeats, so there isn't much to comment here. 
    print("Your word choices are " + str(randomword))
    guess1 = input("Guess the first word: ")
    if guess1 == word:
        print("Correct! You Win!")
    else:
        print("Sorry, incorrect.")
        print("—--------------|")
        print("|              |")
        print("|              @")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
        print("Try again.")
        print("Your word choices are " + str(randomword))
        guess2 = input("Guess the word: ")
    if guess2 == word:
        print("Correct! You Win!")
    else:
        print("Sorry, incorrect.")
        print("—--------------|")
        print("|              |")
        print("|              @")
        print("|             /| ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
        print("Try again.")
        print("Your word choices are " + str(randomword))
        guess3 = input("Guess the word: ")
        if guess3 == word:
         print("Correct! You Win!")
        else:
             print("Sorry, incorrect.")
        print("—--------------|")
        print("|              |")
        print("|              @")
        print("|             /| ")
        print("|             /   ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
        print("Try again.")
        print("Your word choices are " + str(randomword))
        guess4 = input("Guess the word: ")
        if guess4 == word:
         print("Correct! You Win!")
        else:
            print("Sorry, incorrect.")
        print("—--------------|")
        print("|              |")
        print("|              @")
        print("|             /|\ ")
        print("|             /   ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
        print("Try again.")
        print("Your word choices are " + str(randomword))
        guess5 = input("Guess the word: ")
        if guess5 == word:
         print("Correct! You Win!")
        else:
           print("Sorry, incorrect.")
        print("—--------------|")
        print("|              |")
        print("|              @")
        print("|             /|\ ")
        print("|             / \  ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
        print("You lost :(. The correct word was " + word)
elif word_or_letter == "letter":
    win = 0 
    guessl1 = input("What is your first letter guess?")
    if guessl1 in word:
        print("That is correct!")
        win = win + 1
    else:
        print("Sorry, Incorrect.")
        print("—--------------|")
        print("|              |")
        print("|              @")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
        guessl2 = input("What is your second letter guess?")
        if guessl2 in word:
            print("That is correct!")
            win = win + 1
        else:
            print("Sorry, Incorrect.")
            print("—--------------|")
        print("|              |")
        print("|              @")
        print("|             /| ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
        guessl3 = input("What is your third letter guess?")
        if guessl3 in word:
            print("That is correct!")
            win = win + 1
        else: 
            print("Sorry, Incorrect.")
            print("—--------------|")
        print("|              |")
        print("|              @")
        print("|             /| ")
        print("|             /   ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
        guessl4 = input("What is your fourth letter guess?")
        if guessl4 in word:
            print("That is correct!")
            win = win + 1
        else:
            print("Sorry, Incorrect")
            print("—--------------|")
        print("|              |")
        print("|              @")
        print("|             /|\ ")
        print("|             /   ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("—----—-----------")
            
            
            
        
# If the user inputs a term that is not "word" or "letter" they will be met with this error. Letter and Word should be all lowercase
else:
   print("Error! You can only choose between a letter or word. (If you got here by accident try using all lowercase or check your spelling.)")