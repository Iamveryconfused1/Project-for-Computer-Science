import random
# Imports the randint command. This is what randomly selects the word for you. 

print("Welcome to Luka's Hangman! Ready to play?")
print("Choosing a random word...")

# List of possible words that can be used (Amount is 25)
randomword = ["spit", "scrap", "rent", "hut", "fade", "slide", "sell", "budget", "tension", "boat", "drain", "winter", "anticipation", "body", "blue", "seed", "correspondence", "dough", "diplomat", "prevent", "calf", "stretch", "mountain", "float", "active", "museum"]

# Chooses the word from the list above randomly.
word = randomword[random.randint(0, 24)]

# Asks user for what type of game they want; letter guessing or word guessing.
word_or_letter = input("Would you like to guess a word or letter? ")
if word_or_letter == "word":
   
   # Prompts the user for first word guess. If correct, they win. If incorrect, we start hanging the man. The code repeats, so there isn't much to comment here. 
    print("Your word choices are" + str(randomword))
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
        print("Your word choices are" + str(randomword))
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
        print("Your word choices are" + str(randomword))
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
        print("Your word choices are" + str(randomword))
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
        print("Your word choices are" + str(randomword))
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
if word_or_letter == "letter":
   # Prompts the user for first letter guess. If correct, they win. If incorrect, we start hanging the man. The code repeats, so there isn't much to comment here. 
   # WARNING! This is kinda broken. I am still working on it, so I would not use it unless you are somehow magical; you would need to guess every letter correctly IN A ROW
   lguess1c = input("Guess the first letter.")
   if lguess1c == word[0]:
      print("Correct!")
      lguess2c = input("What is the second letter?")
      if lguess2c == word[1]:
         print("Correct!")
         lguess3c = input("What is the third letter?")
         if lguess3c == word[2]:
          print("Correct!")
         lguess4c = input ("What is the fourth letter?")
         if lguess4c == word[3]:
            print("Correct!")
            lguessfinalc = input("What is your final guess?")
            if lguessfinalc == word[4]:
               print("Congrats! You win!")

# If the user inputs a term that is not "word" or "letter" they will be met with this error. Letter and Word should be all lowercase
else:
   print("Error! You can only choose between a letter or word. (If you got here by accident try using all lowercase or check your spelling.)")
      