def display(correct_letters,wrong_letters,word):
  print(hangman_imgs([len(wrong_letters)])
  print("Wrong:"\n)
  for w in wrong_letters:
    print(guess, end='')

while tries < 6:
  game_over = False

  blanks = "_" * len(secret_word)
def update(word):

    strikes = 0

    word_display = []
 
    correct_letters = []
 
    wrong_letters = []
 
    strikes = 0
 
    hangman_imgs = ['A','B','C','D','E','F']
    '''To be replaced with actual images provided by Greg'''
    # Stores the hangman's body values to be shown to the player
    #hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

for s in range(len(secret_word)):
 if guess[s] in correct_letters:  
   blanks = blanks[:s] + secretWord[s] + blanks[s+1:]
  else: 
    print("Incorrect.")
    failed += 1
 
 for b in blanks: 
  print(letter, end=' ')
  print()

for g in guess:

   if guess in word:
      
      print(guess)
      print()

   
if failed == 0:
   print ("You won" )

# exit the script
   break

print
# ask the user go guess a character
guess = input("guess a character:")

# set the players guess to guesses
guesses += guess

# if the guess is not found in the secret word
if guess not in word:

# turns counter decreases with 1 (now 9)
turns -= 1

# print wrong
print ("Wrong")

# how many turns are left
print("You have", + turns, 'more guesses' )

# if the turns are equal to zero
   if turns == 0:

   # print "You Loose"
   print ("You Loose")