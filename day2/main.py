import random 



word_list = ["aardvark", "baboon", "camel"]
stages=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=0
print("Welcome to the Hangeman Game! HAHAHAHHAHAaahaa")
print("hello")
word_chosen= random.choice(word_list)

empty_word =[] 

for char in word_chosen:
    empty_word+="_"



while not lives:
    print(f"word to guess is: {"".join(empty_word)}")
    guess=input(f"Guess a letter:")
    if empty_word==word_chosen:
            print("You Win")

    if guess in word_chosen:
        for i in range(len(word_chosen)):
            if guess == word_chosen[i]:
                empty_word[i]=word_chosen[i]
    else:
        print(f"You guess {guess}, That's not in the word. You lose a life.")
        lives+=1
        print(stages[lives])
    
    

