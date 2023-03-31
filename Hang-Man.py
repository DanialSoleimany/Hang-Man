import random

# Hang-Man Game
def hang_man(): 

    words = ["magical", "matrix", "lovely", "master", "life", "heavy", "trip", "university", "shake", "boss", "make", "hobby", "future", "dream", "sequence", "terrible", "guy", "perfect", "killer", "fake", "body", "heart", "english", "polite", "secret", "never", "guilty", "seperate", "gun", "sheep", "turn", "hard", "day", "fun", "wear", "rank"]
    random_word = random.choice(words)
    listed_word = list(random_word)
    copy_word = listed_word.copy()
    blank = len(random_word) * "_"
    listed_blank = list(blank)
    guess_limit = 15
    generated_word = blank

    user_name = input("\nWhat's your name ?\n")
    print(f"\nHey {user_name}!\nWelcome to this game :)\nI hope you enjoy...")

    while guess_limit > 0 :

        print(f"\nWord to guess is {generated_word}")

        if listed_blank == copy_word:
            print(f"Congrats {user_name}! You Win!\n")
            break
        
        user_guess = input("Guess a character:\n")
        
        if user_guess in listed_word: 
            index = listed_word.index(user_guess)
            listed_word.pop(index)
            listed_word.insert(index, "_")
            listed_blank.pop(index)
            listed_blank.insert(index, user_guess)

        else:
            guess_limit -= 1
            if guess_limit > 0:
                print(f"\nGuess again {user_name}! You have {guess_limit} more chances")

        if guess_limit == 0:
            print(f"\nYou Lose {user_name}!\nThe word is {random_word}\n")

        generated_word = "".join(listed_blank)
    
hang_man()