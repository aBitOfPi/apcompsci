secretWord = input("what word do you want? ")
global wrongAnswer
wrongAnswer = 6
letters = list(secretWord)

wordLength = len(secretWord)
correctGuesses = 0 

for i in range(wrongAnswer):
  letterGuess = input("Guess a letter ")
  if letterGuess in secretWord: 
    locations = []
    for i in range(wordLength):
      if secretWord.startswith(letterGuess, i):
          locations.append(i)
    correctGuesses = correctGuesses + 1
    print("That it correct! That letter appears in the word at positions" + str(locations))
  elif letterGuess not in secretWord:
    print("That is not in the word! :(")

finalGuess = input("You have no more hints!\nWhat is your final guess? ")
if finalGuess == secretWord: 
  print("You Win!")
else:
  print("You lose! The word was " + secretWord)
                  