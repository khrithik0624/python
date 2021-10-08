from words import words
import random
import string

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the given word
    alphabet = set(string.ascii_uppercase) # all upper case alphabets
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print("You have ",lives," left and You can use these letters: "," ".join(alphabet - used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("The current word is: "," ".join(word_list))
        user_letter=input("   GUESS A LETTER:  ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else :
                lives = lives -1
                print("Letter not in the word!!!")
        
        elif user_letter in used_letters:
            print("You have already used that word!!!!")
        
        else:
            print("Invalid Character!!!")
    if lives == 0:
        print(f"The word was {word} . The hangman died!!!")
    else:
        print(f"The word was {word} . Congrats you have saved the hangman !!!")
        

     
    

hangman()