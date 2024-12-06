letter_to_number = {
  'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 
  'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 
  'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

keyLetters = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 
      'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 
      'V', 'K', 'J', 'X', 'Q', 'Z']

def decrypt(userText):
  decryptedString = ""
  userText = userText.upper()

  letter_count = {}
  for char in userText:
      if char.isalpha():
          if char in letter_count:
              letter_count[char] += 1
          else:
              letter_count[char] = 1

  most_common = None
  max_count = 0
  for letter, count in letter_count.items():
      if count > max_count:
          most_common = letter
          max_count = count

  
  shiftKey = (letter_to_number[most_common] - letter_to_number[keyLetters[0]]) % 26

  userText = userText.lower()
  for letter in userText:
      if letter.isalpha():
          new_letter = chr((ord(letter) - ord('a') - shiftKey) % 26 + ord('a'))
          decryptedString += new_letter
      else:
          decryptedString += letter

  return decryptedString

userText = str(input("What would you like me to decrypt? "))
attempts = int(input("How many attempts would you like to try? (up to 26) "))
for i in range(attempts):

  print(f"Testing the letter {keyLetters[0]}: {decrypt(userText)}")
  print("")

  keyLetters.append(keyLetters.pop(0))