def encrypt(userString, shiftKey):
  encryptedString = ""
  userString = userString.lower()

  for i in range(len(userString)):
      letter = userString[i]
      new_letter = chr((ord(letter) + 7 + shiftKey) % 26 + ord('a'))
      encryptedString += new_letter

  return encryptedString

playing = True
while playing:
  userString = str(input("What would you like to encrypt? "))
  shiftKey = int(input("What would you like the key to be? "))

  print(encrypt(userString, shiftKey))
  playing = bool(input("Encrypt something else (True/False)? "))

