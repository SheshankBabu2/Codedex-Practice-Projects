import random

word_bank = ['computers', 'networking', 'games','unity','bui']
word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

attempts = 15

while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  guess = input('Guess a letter: ')
  
  if guess in word:
    for i in range(len(word)):
      if word[i]  == guess:
        guessedWord[i] = guess
    print('Great guess!')
  else:
    attempts -=  1 
    print('Wrong guess! Attempts Left: ' + str(attempts))
  
  if '_' not in guessedWord:
    print('\nCongratulations!! You guessed the Word: '+ word)
    break
else:
    print('\nYou\'ve run out of attempts! The word was: '+ word)
