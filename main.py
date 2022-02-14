def update(word):

    strikes = 0 # <-- Do I need this?

    word_display = []
 
    correct_letters = []
 
    wrong_letters = []
 
    hangman_imgs = ['A','B','C','D','E','F']
    '''To be replaced with actual images provided by Greg'''
   
def display(correct_letters,wrong_letters,word):
  print(hangman_imgs([len(wrong_letters)]) +  print("Wrong:")
  
  for w in wrong_letters:
    print(guess, end='')


while strikes < 6:
  game_over = False

  blanks = "_" * len(secret_word)

  for s in range(len(secret_word)):
  if guess[s] in correct_letters:  
    blanks = blanks[:s] + secretWord[s] + blanks[s+1:]
    else: 
      hangman_imgs = hangman_imgs[+1]
      strikes += 1
      wrong_letters = guess.append()
      print("Incorrect.")
      print(hangman_imgs)
  
  for b in blanks: 
    print(letter, end=' ')
    print()
    '''Not so sure about this section'''
    
  if strikes == 6:
    game_over = True
    print ("GAME OVER")
  elif blanks == 0:
    print("VICTORY!") 
  elif blanks == 0 and strikes == 0:
    print("VICTORY! You're one smart cookie!") 


# 7#07_73|\|